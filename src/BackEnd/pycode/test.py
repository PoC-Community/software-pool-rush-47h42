import os, re

class Report:

    def __init__(self, config):
        self.date = config[0]
        self.id = config[1]
        self.user = config[2]
        self.test = config[3]
        self.reponame = config[4]
        self.pname = self.getpname()

    def getpname(self):
        i = len(self.reponame) - 1
        while(self.reponame[i] and self.reponame[i] != '/'):
            i -= 1
        return self.reponame[i + 1:][:-4]

    def dir(self):
        os.system('mkdir ' + self.user + self.test + self.date)
        os.chdir(self.user + self.test + self.date)
        os.system('touch cctrace.json maintrace.json')
        self.ccreportfile = open('ccreport.json', 'w') #file de cc report
        return self.user + self.test + self.date

    def pull_repo(self):
        cmd = os.popen('git clone ' + self.reponame)
        self.repo_pull_log = cmd.read()

    def csreport(self):
        os.chdir(self.pname)
        cmd = os.popen('../../Banana/banana')
        self.csreportlog = cmd.read()
        os.chdir('..')

    def makereport(self):
        os.chdir(self.pname)
        cmd = os.popen('make')
        self.makereportlog = cmd.read()
        os.chdir('..')

    def ccreport_gen(self):
        Report = []
        self.csreport()
        self.makereport()
        error = (len(re.findall('\n', self.csreportlog)) - 2) / 2
        Report.append({'CodingStyle Error': str((error - 2) / 2)})
        Report.append({'Compilation Report': self.makereport})
        json.

    def destroy(self):
        pass #fermeture de tout les fichiers

rep = Report("date id user test https://github.com/basileft/My_Radar.git".split())
# print(rep.getpname())
rep.dir()
rep.pull_repo()
rep.ccreport_gen()