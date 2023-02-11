import os, re, json, subprocess

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
        os.system('mkdir ' + self.id)
        os.chdir(self.id)
        os.system('touch cctrace.json ')
        self.ccreportfile = open('cctrace.json', 'w') #file de cc report
        return self.id

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
        self.makereportlog = subprocess.run(['make'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        os.chdir('..')

    def ccreport_gen(self):
        Report = []
        self.csreport()
        self.makereport()
        self.main_test()
        error = (len(re.findall('\n', self.csreportlog)) - 2) / 2
        Report.append({'CodingStyle Error': int((error - 2) / 2)})
        Report.append({'Compilation Report': str(self.makereportlog)})
        json.dump(Report, self.ccreportfile, indent=4)

    def main_test(self):
        os.chdir(self.pname)
        os.system('../../TESTERS/' + self.test + '/tester.py')

    def destroy(self):
        os.chdir('../..')
        # os.system('rm -rf ' + self.id)
