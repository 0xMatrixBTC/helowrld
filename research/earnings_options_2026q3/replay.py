# Replay: buy today (close 2026-10-12) at today's option prices; for each past earnings event,
# apply the stock's actual path over the same window (entry = same # of trading days before the
# reaction day as today is; exit = option expiry offset). Payoff at expiry vs premium paid.
import statistics as st
dates=open('dates.txt').read().split(); idx={d:i for i,d in enumerate(dates)}
ev={}
for line in open('results.txt'):
    p=line.split()
    if p and ':' in line and p[0].isupper(): ev[p[0]]=['20'+x.split(':')[0] for x in p[1:]]
# tkr: spot, K_atm, call, put, K_otm, otm_call, reaction_offset, expiry_offset, assumed earnings
D={
'TSLA':(378.03,375,15.325,11.75,412.5,3.325,8,9,'10/21 AMC (confirmed)'),
'COIN':(180.39,180,10.80,10.05,200,4.225,14,14,'~10/29 AMC (est.)'),
'INTC':(101.35,101,6.275,5.675,111,2.88,14,14,'10/29 AMC (likely)'),
'PLTR':(209.00,210,12.45,12.85,230,5.375,16,19,'~11/2 AMC (est.)'),
'AMD': (594.24,595,34.375,33.25,650,14.975,17,19,'~11/3 AMC (est.)'),
'SNAP':(6.53,6.5,0.625,0.585,7.5,0.32,18,19,'~11/4 AMC (est.)'),
}
print(f"{'Tkr':5}{'Earnings':>22}{'N':>3}{'Straddle%':>10}{'RealAbs%':>9}{'Real/Impl':>10}{'StradRet':>9}{'StradWin':>9}{'OTMcall':>8}{'CallRet':>9}{'CallWin':>8}{'BestCall':>9}")
for t,(S,K,c,p,Ko,co,ro,eo,lab) in D.items():
    c0=[float(x) for x in open(f'{t}.txt').read().strip().split(',')]
    moves=[]
    for d in ev[t]:
        r=idx[d]; e=r-ro; x=e+eo
        if e<0 or x>=len(c0): continue
        moves.append(c0[x]/c0[e]-1)
    strad=c+p
    sp=[abs(S*(1+m)-K) for m in moves]; cp=[max(S*(1+m)-Ko,0) for m in moves]
    print(f"{t:5}{lab:>22}{len(moves):3d}{strad/S*100:9.1f}%{st.mean(abs(m) for m in moves)*100:8.1f}%{st.mean(abs(m) for m in moves)/(strad/S):10.2f}"
          f"{st.mean(sp)/strad-1:+9.0%}{sum(x>strad for x in sp):6d}/{len(moves)}{Ko:8g}{st.mean(cp)/co-1:+9.0%}{sum(x>co for x in cp):5d}/{len(moves)}{max(cp)/co-1:+9.0%}")
    print('      window moves:',' '.join(f'{m*100:+.1f}%' for m in moves))
