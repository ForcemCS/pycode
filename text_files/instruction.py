# 什么是Context?
# 可以理解为一段有明确开始和结束的代码区域,当你进入这段代码区域时，有些事情会发生；当你离开另一些事情会发生.
# 它就像一个“迷你世界”或“事务”，在这个世界里，你可能需要一些资源，当你离开时，这些资源需要被妥善处理

# 什么是Context Manager?
# 上下文管理器（Context Manager）是一个 Python 对象，它负责管理进入和退出特定上下文时需要执行的操作。
# 简单来说，它就像一个“管家”，帮你处理好资源的申请（在进入时）和释放（在退出时），确保无论代码如何执行（即使发生错误），资源都能被正确清理。
# 它的核心作用是： 确保资源被安全地分配和释放。这对于避免资源泄露（例如，忘记关闭文件或释放锁）至关重要。


# 在 Python 中，我们通常使用 with 语句来“调用”和使用上下文管理器。
# with 语句是使用上下文管理器最常见、最推荐的方式，因为它简洁、安全，并且Python解释器会保证在 with 代码块结束时自动调用上下文管理器的退出方法，无论代码是正常执行完成还是中间发生了异常。


# 写入文件
with open("hello.txt", "w") as f:
    f.write("Hello, Python learners!\n")
    f.write("Context managers are great!\n")
# 文件在 with block 结束后自动关闭

print("文件写入完成。")

# 读取文件
with open("hello.txt", "r") as f:
    for line in f:
        print(line.strip()) # strip() 用于移除行末的换行符
# 文件在 with block 结束后自动关闭

print("文件读取完成。")