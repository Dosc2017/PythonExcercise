

s = ['adcd', 'adddd']


# Return the longest prefix of all list elements.
def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    # Some people pass in a list of pathname parts to operate in an OS-agnostic
    # fashion; don't try to translate in that case as that's an abuse of the
    # API and they are already doing what they need to be OS-agnostic and so
    # they most likely won't be using an os.PathLike object in the sublists.

    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):

        if c != s2[i]:
            return s1[:i], s

    return s1


print(commonprefix(s))


b = [1, 4, 3]
for i in b:
    if i > 3:
        print(3)
