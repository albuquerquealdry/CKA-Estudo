import dns.resolver

resolver = dns.resolver.Resolver.resolve(query)

# 8.8.8.8 é o DNS público do Google
resolver.nameservers = ['8.8.8.8']

answers = resolver.query('google.com')

for rdata in answers:
    print (rdata.address)