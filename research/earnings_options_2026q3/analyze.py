import statistics as st
dates = open('dates.txt').read().split()
idx = {d:i for i,d in enumerate(dates)}
anchors = {
 'TSLA':['2024-10-24','2025-01-30','2025-04-23','2025-07-24','2025-10-23','2026-01-29','2026-04-23','2026-07-23'],
 'NFLX':['2024-10-18','2025-01-22','2025-04-21','2025-07-18','2025-10-22','2026-01-21','2026-04-17','2026-07-17'],
 'META':['2024-10-31','2025-01-30','2025-05-01','2025-07-31','2025-10-30','2026-01-29','2026-04-30','2026-07-30'],
 'PLTR':['2024-11-05','2025-02-04','2025-05-06','2025-08-05','2025-11-04','2026-02-03','2026-05-05','2026-08-04'],
 'AMD': ['2024-10-30','2025-02-05','2025-05-07','2025-08-06','2025-11-05','2026-02-04','2026-05-06','2026-08-05'],
 'COIN':['2024-10-31','2025-02-14','2025-05-09','2025-08-01','2025-10-31','2026-02-13','2026-05-08','2026-07-31'],
 'INTC':['2024-11-01','2025-01-31','2025-04-25','2025-07-25','2025-10-24','2026-01-23','2026-04-24','2026-07-24'],
 'SNAP':['2024-10-30','2025-02-05','2025-04-30','2025-08-06','2025-11-06','2026-02-05','2026-04-29','2026-08-05'],
}
W=3
confirmed={('TSLA','2026-07-23'),('PLTR','2026-02-03'),('PLTR','2026-05-05'),('PLTR','2026-08-04'),('COIN','2026-07-31')}
rows=[]
for t,anc in anchors.items():
    c=[float(x) for x in open(f'{t}.txt').read().strip().split(',')]
    r=[None]+[c[i]/c[i-1]-1 for i in range(1,len(c))]
    ev=[]; used=set()
    for a in anc:
        i=idx[a]
        w=0 if (a<'2026' or (t,a) in confirmed) else 1
        cand=[j for j in range(max(1,i-w),min(len(c),i+w+1))]
        excl=[k for k in range(max(1,i-3),min(len(c),i+4))]
        j=max(cand,key=lambda k:abs(r[k]))
        ev.append((dates[j],r[j])); used.update(excl)
    normal=[abs(r[k]) for k in range(1,len(c)) if k not in used]
    absm=[abs(x) for _,x in ev]
    up=sum(1 for _,x in ev if x>0)
    big=sum(1 for x in absm if x>=0.10)
    rows.append((t,st.mean(absm),st.median(absm),max(absm),min(absm),st.mean(normal),up,big,ev))
rows.sort(key=lambda x:-x[1])
print(f"{'Tkr':5}{'AvgAbs':>8}{'Median':>8}{'Max':>8}{'Min':>7}{'NormDay':>9}{'Ratio':>7}{'Up/8':>6}{'>=10%':>6}")
for t,a,m,mx,mn,nd,up,big,ev in rows:
    print(f"{t:5}{a*100:7.1f}%{m*100:7.1f}%{mx*100:7.1f}%{mn*100:6.1f}%{nd*100:8.2f}%{a/nd:7.1f}{up:6d}{big:6d}")
print()
for t,*_,ev in rows:
    print(t,' '.join(f"{d[2:]}:{x*100:+.1f}%" for d,x in ev))
