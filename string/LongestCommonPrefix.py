def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs:
        return ""
    prefix = strs[0]
    has_prefix = 1

    while prefix:
        for w in strs:
            if not w.startswith(prefix):
                has_prefix = 0
                break
        if has_prefix:
            break;
        else:
            prefix = prefix[:-1]
            has_prefix = 1
    return prefix

print(longestCommonPrefix(["shu","sku"]))