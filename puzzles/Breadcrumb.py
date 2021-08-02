"""
https://www.codewars.com/kata/563fbac924106b8bf7000046/train/python
"""

class Solution:
    def solution(self, url, separator):
        """
        overview: 
        strip up to first / and replace with HOME
        pull each subsequent element up to the next / and create an UPPER label <a> for it
        final element is the same but <span> instead of <a>

        notes:
        ignore final .htm .php etc if it is present (check for .)
        if last element is index.anything, omit it entirely
        if any elemet longer than 30 char, shorten it to an acronym (words will be separated by '-', like-this-example)
        ignore anchors after # (they/look/like#this) and parameters after ? (like.com?yes=true)
        """

        
        
        return True