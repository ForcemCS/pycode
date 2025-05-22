#异常类层级图 https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#Python 中所有的异常都是 类（class），而且这些类之间是有“父子关系”的 —— 这就是所谓的“层级”。
#就像你有个姓“张”的家族，张三、张四、张五都是这个家族的一员，但每个人的身份又不同。
#异常是一种特殊的object类型，例如ValueError是

##py中有许多内置的exception type ，请参考https://docs.python.org/3/library/exceptions.html


#raise Exception (主动抛出异常)。
# 想象一下，你正在编写一个函数，这个函数有一些特定的要求或前提条件。如果调用者没有满足这些条件，你的函数可能就无法正常工作，或者会产生错误的结果。
# 在这种情况下，与其让函数静默地失败或返回一个奇怪的值，不如在发现问题时主动地通知调用者：“嘿，出问题了！你给我的条件不对”
# 这个“主动通知”的动作，就是通过 raise 语句来抛出一个异常。
#raise 的基本语法：
##raise [ExceptionType([args])]
###ExceptionType: 你想要抛出的异常的类型 (例如 ValueError, TypeError, 或者是你自己定义的异常类)。
###args (可选): 传递给异常构造函数的参数，通常是一个描述错误信息的字符串。