from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 🔍 Step 1: Find the maximum citation count
        maxNoofCitations = max(citations)

        # 🧮 Step 2: Create a frequency array to count how many papers have exactly i citations
        citationCount = [0] * (maxNoofCitations + 1)

        # 📊 Step 3: Populate the citation count array
        for citation in citations:
            citationCount[citation] += 1

        # ➕ Step 4: Convert the array to represent cumulative counts
        # citationCount[i] will then represent the number of papers with at least i citations
        for currentCitation in range(maxNoofCitations - 1, 0, -1):
            citationCount[currentCitation] += citationCount[currentCitation + 1]

        # 🎯 Step 5: Find the highest h such that at least h papers have >= h citations
        for currentCitation in range(maxNoofCitations, 0, -1):
            if citationCount[currentCitation] >= currentCitation:
                return currentCitation  # ✅ h-index found

        # 🚫 Step 6: If no valid h-index is found, return 0
        return 0

sol = Solution()
print(sol.hIndex([1,3,1]))