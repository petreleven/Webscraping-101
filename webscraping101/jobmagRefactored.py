import requests
import bs4

print('Loading page...')
url=f'https://www.myjobmag.co.ke/search/jobs?q=&field=Engineering+%2F+Technical'

def getJobtitle(soup):
    title=soup.select('section h1')
    return str(title[0].getText())


def getDescription(soup):
     Description=soup.select('.job-details p')
     return str(Description[0].getText())


def getAcademics(soup):
    Academics=soup.select('.job-key-info span')
    return str(Academics[3].getText())


def getExperience(soup):
    Experience=soup.select('.job-key-info span')
    return str(Experience[5].getText())


def save_job_info(JobTitle,JobDescription,JobAcademics,JobExp,job_Link):
    print('Saving job specifications...')
    jobfile=open('C:\\Users\\peter\\Desktop\\spicebucks\\Jobmag scrapped.txt','a')
    jobfile.write('Tittle :'+JobTitle+'\n'+'Descrition :'+JobDescription+'\n'+'Academics :'+JobAcademics+'\n'+'Experience'+str(JobExp)+'\n')
    jobfile.write(job_Link+'\n'+'*'*70)
    jobfile.close()  

def mainfunc():
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    elems=soup.select('section a')

    for i in range (1,35,2):
        jobUrl=requests.get('https://www.myjobmag.co.ke'+elems[i].get('href'))
        job_Link='https://www.myjobmag.co.ke'+elems[i].get('href')
        jobUrl.raise_for_status()
        soup=bs4.BeautifulSoup(jobUrl.text,'html.parser')
        print('Getting job specifications...')
        
        JobTitle=getJobtitle(soup)
        JobDescription=getDescription(soup)
        JobAcademics=getAcademics(soup)
        JobExp=getExperience(soup)

        save_job_info(JobTitle,JobDescription,JobAcademics,JobExp,job_Link)



mainfunc()
print('Done') 
    





