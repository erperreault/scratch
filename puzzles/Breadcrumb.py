"""
https://www.codewars.com/kata/563fbac924106b8bf7000046/train/python
&lt;a href="/"&gt;HOME&lt;/a&gt; : &lt;a href="/skin-and-eurasian-eurasian/"&gt;SKIN-AND-EURASIAN-EURASIAN&lt;/a&gt; : &lt;span class="active"&gt;WEB&lt;/span&gt;
&lt;a href="/"&gt;HOME&lt;/a&gt; : &lt;a href="/skin-and-eurasian-eurasian/"&gt;SKIN AND EURASIAN EURASIAN&lt;/a&gt; : &lt;span class="active"&gt;WEB&lt;/span&gt;
"""

class Solution:
    def solution(self, url, separator):
        print(url)
        l = self.cleanup(url)
        print(l)
        if len(l) > 1:
            solution = '<a href="/">HOME</a>' + separator
        else:
            return f'<span class="active">HOME</span>'

        href = '/'
        for a in l[1:-1]:
            href += a + '/'
            if len(a) > 30:
                a = self.acronym(a)
            a = a.replace('-', ' ')
            solution += f'<a href="{href}">{a.upper()}</a>' + separator
        
        if len(l[-1]) > 30:
                l[-1] = self.acronym(l[-1])
        l[-1] = l[-1].replace('-', ' ')
        solution += f'<span class="active">{l[-1].upper()}</span>'

        return solution
        
    def cleanup(self, url):
        l = url.split('/')
        if 'http' in l[0]:
            l = l[2:]
        if 'www' in l[0]:
            l[0] = l[0].split('.')[1]
        else:
            l[0] = l[0].split('.')[0]
        
        if len(l) == 1:
            return l

        for anchor in ['#', '?']:
            if anchor in l[-1]:
                l[-1] = l[-1].split(anchor)[0]

        if 'index.' in l[-1]:
            l.pop()
        else:
            if '.' in l[-1]:
                l[-1] = l[-1].split('.')[0]

        while '' in l:
            l.remove('')
            
        return l

    def acronym(self, s):
        ignore = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]

        s_split = s.split('-')
        b = [ c[0] for c in s_split if c not in ignore ]
        a = ''.join(b)

        return a