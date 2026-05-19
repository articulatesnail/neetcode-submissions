class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_stripped = []
        for email in emails:
            stripped = self.stripEmail(email)
            if stripped not in emails_stripped:
                emails_stripped.append(stripped)
        return len(emails_stripped)
    
    def stripEmail(self, email: str) -> str:
        local, domain = email.split("@")
        localBase = local.split("+")[0].replace(".","")
        strippedEmail = localBase+"@"+domain
        return strippedEmail




        