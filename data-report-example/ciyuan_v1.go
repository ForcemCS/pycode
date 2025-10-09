package main

import (
	"database/sql"
	"fmt"
	"log"
	"strings"
	"time"

	_ "github.com/go-sql-driver/mysql" // MySQL 驱动
)

// --- 配置 ---
// 强烈建议在生产环境中使用环境变量或配置文件
const (
	DBUser     = "readonly"
	DBPassword = "xxxx"      // 替换为您的密码
	DBHost     = "xxxxxxxxx" // 替换为您的主机
	DBPort     = "xxxxxxxxx" // 替换为您的端口
	DBName     = "db_ro3_operation_log"
)

// --- 常量定义 ---
var (
	ExcludeUIDSuffixes = []string{"40001", "40002", "40003", "40004", "40990"}
	TargetWhereClause  = "CMD_Dimension_Crack_GetReward_REQ"
)

// InitialPlayer 用于存储第一阶段查询的结果
type InitialPlayer struct {
	UID         string
	CreateStamp time.Time
	CheckDate   string // YYYY-MM-DD 格式
}

// QualifiedPlayer 用于存储最终结果
type QualifiedPlayer struct {
	UID             string
	CreateStamp     time.Time
	CheckedLogTable string
}

func main() {
	finalList, err := findQualifiedPlayers()
	if err != nil {
		log.Fatalf("执行查询时发生致命错误: %v", err)
	}

	fmt.Println("\n==============================================")
	if len(finalList) > 0 {
		fmt.Printf("最终找到 %d 位符合所有条件的玩家:\n", len(finalList))
		for _, player := range finalList {
			fmt.Printf("UID: %s, 创角时间: %s, 检查表: %s\n",
				player.UID, player.CreateStamp.Format("2006-01-02 15:04:05"), player.CheckedLogTable)
		}
	} else {
		fmt.Println("未找到符合所有条件的玩家。")
	}
	fmt.Println("==============================================")
}

func findQualifiedPlayers() ([]QualifiedPlayer, error) {
	// 构造数据库连接字符串 (DSN)
	// parseTime=true 是必须的，以便将数据库中的 DATETIME/TIMESTAMP 类型正确解析为 time.Time
	dsn := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?charset=utf8mb4&parseTime=true",
		DBUser, DBPassword, DBHost, DBPort, DBName)

	db, err := sql.Open("mysql", dsn)
	if err != nil {
		return nil, fmt.Errorf("数据库连接配置错误: %w", err)
	}
	defer db.Close()

	// 检查数据库连接是否成功
	if err := db.Ping(); err != nil {
		return nil, fmt.Errorf("无法连接到数据库: %w", err)
	}

	// --- 阶段 1: 查找满足静态条件的玩家 ---
	log.Println("--- 阶段 1: 正在查询符合付费和等级条件的玩家 ---")

	// 构造排除后缀的字符串，例如: '40001','40002',...
	var quotedSuffixes []string
	for _, s := range ExcludeUIDSuffixes {
		quotedSuffixes = append(quotedSuffixes, fmt.Sprintf("'%s'", s))
	}
	excludeListStr := strings.Join(quotedSuffixes, ", ")

	part1SQL := fmt.Sprintf(`
		SELECT
			R.uid,
			R.create_stamp,
			DATE_FORMAT(DATE_ADD(DATE(R.create_stamp), INTERVAL 1 DAY), '%%Y-%%m-%%d') AS check_date
		FROM db_ro3_operation_log.SNAP_ROLE R
		JOIN (
			SELECT DISTINCT uid FROM db_ro3_sdk2.T_ORDER
			WHERE status = 2 AND site_id = 4 AND RIGHT(uid, 5) NOT IN (%s)
		) AS Qualified_Paid ON R.uid = Qualified_Paid.uid
		JOIN db_ro3_operation_log.level_change_log L ON R.uid = L.uid
		WHERE DATE(L.time_stamp) = DATE(R.create_stamp) AND L.lv_type = 1
		GROUP BY R.uid, R.create_stamp
		HAVING MAX(L.after_lv) = 36
	`, excludeListStr) // 注意：这里拼接是安全的，因为来源是常量

	rows, err := db.Query(part1SQL)
	if err != nil {
		return nil, fmt.Errorf("执行阶段1查询失败: %w", err)
	}
	defer rows.Close()

	var initialPlayers []InitialPlayer
	for rows.Next() {
		var p InitialPlayer
		if err := rows.Scan(&p.UID, &p.CreateStamp, &p.CheckDate); err != nil {
			log.Printf("警告: 扫描阶段1数据行失败: %v", err)
			continue
		}
		initialPlayers = append(initialPlayers, p)
	}
	log.Printf("找到 %d 位初步符合条件的玩家。\n", len(initialPlayers))

	if len(initialPlayers) == 0 {
		return nil, nil
	}

	// --- 阶段 2: 动态检查日志 ---
	log.Println("--- 阶段 2: 动态检查创角次日日志记录 ---")
	var qualifiedPlayers []QualifiedPlayer

	for i, player := range initialPlayers {
		logTableName := fmt.Sprintf("item_log_%s", player.CheckDate)

		// SQL注入警告: 表名不能使用参数绑定，必须拼接。
		// 在此场景下是安全的，因为 player.CheckDate 来自于我们自己的数据库查询结果。
		part2SQL := fmt.Sprintf(
			"SELECT 1 FROM `db_ro3_operation_log`.`%s` WHERE uid = ? AND `where` = ? LIMIT 1",
			logTableName,
		)

		var exists int
		err := db.QueryRow(part2SQL, player.UID, TargetWhereClause).Scan(&exists)

		if err == nil {
			// 找到了记录
			qualifiedPlayers = append(qualifiedPlayers, QualifiedPlayer{
				UID:             player.UID,
				CreateStamp:     player.CreateStamp,
				CheckedLogTable: logTableName,
			})
		} else if err == sql.ErrNoRows {
			// 未找到记录，正常情况，什么都不做
		} else {
			// 其他错误，很可能是表不存在 (MySQL error 1146)
			if strings.Contains(err.Error(), "1146") {
				if i%100 == 0 { // 避免日志刷屏
					log.Printf("提示: 日志表 %s 不存在，跳过检查。", logTableName)
				}
			} else {
				log.Printf("警告: 检查日志表 %s 时出错 (UID: %s): %v", logTableName, player.UID, err)
			}
		}
	}

	return qualifiedPlayers, nil
}
