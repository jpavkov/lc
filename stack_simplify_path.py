"""
Given a string path, which is an absolute path (starting with a slash '/') 
to a file or directory in a Unix-style file system, convert it to the 
simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, 
a double period '..' refers to the directory up a level, and any multiple 
consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated 
as file/directory names.

The canonical path should have the following format:
1. The path starts with a single slash '/'.
2. Any two directories are separated by a single slash '/'.
3. The path does not end with a trailing '/'.
4. The path only contains the directories on the path from the 
root directory to the target file or directory (i.e., no period '.' 
or double period '..')

Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation: A double period ".." refers to the directory up a level.

Example 5:
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation: "..." is a valid name for a directory in this problem.

Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        folder_names = path.split("/")

        for folder in folder_names:
            if folder in ('', '.'):
                pass
            elif folder == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(folder)

        return "/" + "/".join(stack)
    

sol = Solution()

# ex 1
path = "/home/"
print(sol.simplifyPath(path))

# ex 2
path = "/../"
print(sol.simplifyPath(path))

# ex 3
path = "/home//foo/"
print(sol.simplifyPath(path))

# ex 4
path = "/home/user/Documents/../Pictures"
print(sol.simplifyPath(path))

# ex 5
path = "/.../a/../b/c/../d/./"
print(sol.simplifyPath(path))
