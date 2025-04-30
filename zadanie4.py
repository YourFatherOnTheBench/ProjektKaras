def add_node(v, name):
    if name in v.keys():
        return
    else:
        v[name]= {}
def add_edge(V, source, dest, weight):
    if not source in V.keys():
        add_node(V, source)
    if not dest in V.keys():
        add_node(V, dest)
    if not dest in V[source].keys():
        V[source][dest] = weight
    else:
        V[source][dest] += weight

file_path = r"./email-Eu-core.txt"
V = {}
with open(file_path, 'r') as f:
    for line in f:
        u,v = line.split(' ')
        u = int(u)
        v = int(v)
        add_edge(V, u, v, 1)

print(f"Number of nodes: {len(V)}")
print(f"Max outcoming emails: {max( [ len(V[n]) for n in V.keys()])}")
max_mails = max([ len(V[n]) for n in V.keys()])
mail_king = -1
for n in V.keys():
    if len(V[n]) == max_mails:
        print(f"King of the emails is {n}")
        mail_king = n

in_mails = 0
for n in V.keys():
    if mail_king in V[n]:
        in_mails += 1


print(f"Number of incoming emails for {mail_king} is : {in_mails}")