import psutil

cpu=psutil.cpu_freq()
print(cpu)

cpu_core=psutil.cpu_count(logical=False)
print(cpu_core)

memory=psutil.virtual_memory()
print(memory)

disk=psutil.disk_partitions()
print(disk)

net=psutil.net_io_counters()
print(net)

# scpufreq(current=3401.0, min=0.0, max=3401.0)
# 16
# svmem(total=17101266944, available=6000992256, percent=64.9, used=11100274688, free=6000992256)
# [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260)]
# snetio(bytes_sent=2342264830, bytes_recv=5982794300, packets_sent=3037744, packets_recv=4562937, errin=0, errout=0, dropin=0, dropout=0)
# (base) 