#!/bin/usr/env sage

from tqdm import tqdm
n = 24575303335152579483219397187273958691356380033536698304119157688003502052393867359624475789987237581184979869428436419625817866822376950791646781307952833871208386360334267547053595730896752931770589720203939060500637555186552912818531990295111060561661560818752278790449531513480358200255943011170338510477311001482737373145408969276262009856332084706260368649633253942184185551079729283490321670915209284267457445004967752486031694845276754057130676437920418693027165980362069983978396995830448343187134852971000315053125678630516116662920249232640518175555970306086459229479906220214332209106520050557209988693711
ks = []
es = []

with open("output.txt", "r") as f:
	data = f.read()
	data = data.split("\n")
	for d in data:
		try:
			e, k = d.split(":")
		except ValueError:
			continue
		else:
			ks.append(int(k))
			es.append(int(e))
dlogs = []
for i in range(len(ks)):
	k_ = pow(ks[i], -1, es[i])
	temp = (k_ * (es[i] - 1)) % es[i]
	dlogs.append(temp)
phi = crt(dlogs, es)
N = 1
for e in es:
	N *= e

sum_pq = (n + 1 - phi) % N
goal = (2^1024 // N) * N
sum_pq += goal
for i in tqdm(range(goal // N)):
	sum_pq += N

	if Integer(sum_pq^2 - 4 * n).sqrt() in ZZ:
		print("yay")
		break

p = (-Integer(sum_pq^2 - 4 * n).sqrt() + sum_pq) // 2
q = sum_pq - p
assert p * q == n

print(p, q)
