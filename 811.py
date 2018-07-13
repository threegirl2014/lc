from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_map = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domains = domain.split('.')
            for i in range(len(domains)):
                domain_map['.'.join(domains[i:])] += count
        return ['{} {}'.format(v, k) for k, v in domain_map.items()]


if __name__ == '__main__':
    print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))
    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
