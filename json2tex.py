#!python
from __future__ import print_function
import json, sys

reload(sys)
sys.setdefaultencoding('utf-8')

def npuwordvar( word, var ):
    hoge = "\\npu%s" % word
    for _ in var:
        hoge += "{%s}" % _
    return hoge

def npudate(info):
	return npuwordvar("date", [info])

def npuhead():
	return npuwordvar("head", [])

def npuevent(time, info, host):
	return npuwordvar("event", [time, info, host])

def npureport(time, name, title):
	return npuwordvar("report", [time, name, title])

def nputeabreak(time, info):
	return npuwordvar("teabreak", [time, info])

def npudetail(name, school, title, abstract, profile):
	return npuwordvar("detail", [name, school, title, abstract, profile])

def npuhost(number, name):
	return npuwordvar("host", [number, name])

def pdate(item, reportlist):
	return npudate(item["info"])

def phead(item, reportlist):
	return npuhead()

def pevent(item, reportlist):
	return npuevent(item["time"], item["info"], item["host"])

def pdetail(r):
	name = r["enname"] if "enname" in r else r["name"]
	school = (r["enschool"] + ", ") if "enschool" in r else ""
	school = school + r["school"]
	return npudetail(name, school, r["title"],\
		r['abstract'], r['profile'])

def getreportinfo(uid, rlist):
  for i in rlist:
    try:
      if int(i["id"]) == int(uid):
        return i
    except KeyError as ke:
      print("keyerror: %s,%s" %(i, uid))
      return None
  else:
    print("uid:%s not found!" % uid)
    return None;

def preports(item, reportlist):
	reports = item["reports"]
	times = item["times"]
	n = len(reports)
	ret = ""
	for i in range(0, n):
		detail = getreportinfo(reports[i], reportlist)
		if detail == None:
			continue
		ret = ret + npureport(times[i], detail["name"], detail["title"]) +"\n"
		number = 0 if i < n - 1 else (1 if n == 1 else -n)
		ret = ret + npuhost(number, item["host"]) +'\n'
	return ret

def pteabreak(item, reportlist):
	return nputeabreak(item["time"], item["info"])

def newtable(_a, _b):
	return tableend() + "\n" + tablebegin()

operator = {"date":pdate, "head":phead, "event": pevent,
            "reports":preports, "teabreak": pteabreak, "newtable": newtable}

def tablebegin():
	return "\\begin{nputable}"

def tableend():
	return "\\end{nputable}"

def printtable(table, reportlist):
	print(tablebegin())
	for i in table:
		print(operator.get(i["type"])(i, reportlist))
	print(tableend())

def printdetail(table, reportlist):
	for i in table:
		if i["type"] == "reports":
			for j in i["reports"]:
				r = getreportinfo(j, reportlist)
				print(pdetail(r))

def main():
	reports = json.load(open("reports.json", 'r'))
	table = json.load(open("table.json", 'r'))

	# tablelist = [Bunch(_) for _ in table]
	sysold = sys.stdout

	with open("table.tex", 'w') as f:
		sys.stdout = f
		printtable(table, reports)
		sys.stdout = sysold

	with open("reports.tex", 'w') as f:
		sys.stdout = f
		printdetail(table, reports)
		sys.stdout = sysold

if __name__ == '__main__':
	main()