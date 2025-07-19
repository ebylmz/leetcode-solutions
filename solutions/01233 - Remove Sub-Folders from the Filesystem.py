class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Sorting ensures that parent folders come before their subfolders lexicographically
        folder.sort()
        result = []
        for f in folder:
            # Use '/' to avoid accepting the case like "/a/ba".startswith("/a/b" + "/") 
            if len(result) == 0 or not f.startswith(result[-1] + "/"):
                result.append(f)
        
        return result