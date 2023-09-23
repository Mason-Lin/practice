def slidingWindow(s: str):
    # 用合适的数据结构记录窗口中的数据
    window = {}

    left = 0
    right = 0

    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        if c not in window:
            window[c] = 1
        else:
            window[c] += 1

        # 增大窗口
        right += 1

        # 进行窗口内数据的一系列更新
        # ...

        # 判断左侧窗口是否要收缩
        while left < right and window_needs_shrink():
            # d 是将移出窗口的字符
            s[left]

            # 缩小窗口
            left += 1

            # 进行窗口内数据的一系列更新
            # ...


def window_needs_shrink():
    pass
