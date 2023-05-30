from Crypto.Util.number import *
from hashlib import sha256

n = 10062704821953299381118013872150801185961537844013735062723729816732285356100705358600649323566461315936460121971474006636382490147267954403524957329641648597166971422109386356155055136946044289274593499733650926175195907066357111852199392875841285126960021565401231708883244823358341538680107429601826504919277121724245368508883975923612424679085396126426007930485323892792575427880546884827376496706960189483957280312459279432163111106713442839944344090006216431212557750251238690628239418520497259548021246487572401803380458267948812771257052465497658279050643129404242366764506351044512890428445775909511266950499
e = 65537
c = 6245933709656257363090195362770572462957730695374578443647362222476764244871795796112560308570647697163351976596121283936220632500389819833974146452050313064353105464799468180406487679280169757857781050179971454855459423905991571297804274798763255929667823986486001391540735095484799899843702965680793168262964951955737725996015130499409046940675966180167041103810661958107260232947299774185366702450261059269220790212553934010242052899578732292497446984208720801700442345664566246400753919841010931074876235962100899161919944514993496803408143676576118767999216452035397709661584660172071229100514729748164065830627
s = 3385059843362307934004172178580455142596211252623465013057418095367622068617321316072975664333635524225179928220654957320160086932450412387083083235025927787884040623086331993039350976063603043122583824348622919619340553072952515198188247945759764368510290289816287516261930762580464107379813854425201606382192272918065808519468945944309809449613657120113003327218808169775099800298533325329180835922602441763895243302433578492108289993974897976372754960027209422448229921931148361959319753262770338742919299633016594138842047528124748443147704268193710121568350972591340425233153796030713754093794612005372897494387

"""
(a*b)%c = ((a%c) * (b%c))%c
s = (h^dp mod q) + ((((h^dp mod p) - (h^dp mod q)) * 1/q) % p)*q
s mod q = h^dp mod q
s mod p = (h^dp mod q) mod p + (((((h^dp mod p) - (h^dp mod q)) * 1/q) % p)*q) mod p
        = (h^dp mod q) mod p + ((h^dp mod p) - (h^dp mod q)) mod p
        = h^dp mod p

Because (p, q) = 1 so with CRT we will have s = h^dp mod n
"""

se = pow(s, e, n)
"""
se = h^(dp*e) mod n = h + kp mod n
=> se - h = 0 (mod n)
because m = sha256(flag).digest() so h < 2^256, and with coppersmith, we can find h and get kp. Finally, we will calculate GCD(se -h, n) = p and we are done!
"""

h = 96697282815618408627302483684282996008752249334370027415270297846716258548364
p = GCD(se - h, n)
q = n//p
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
flag = pow(c, d, n)
print(long_to_bytes(flag))
#ictf{a_typo_leading_to_private_key_being_cracked...}