import os


# create project for website crawled (folder)
def createProjectDir(directory):
    if not os.path.exists(directory):
        print('Creating directory '+ directory)
        os.makedirs(directory)

# createProjectDir('dribbble')


# create queue and crawl file
def createDataFile(projectName, baseUrl):
    queue = projectName+'/queue.txt'
    crawled = projectName+'/crawled.txt'
    if not os.path.exists(queue):
        writeFile(queue, baseUrl)
    if not os.path.exists(crawled):
        writeFile(crawled, '')

# create a new file
def writeFile(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# createDataFile('dribbble','https://dribbble.com/')

# add data into existing file
def appendToFile(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete the contents of a file
def deleteFileContents(path):
    with open(path, 'w'):
        pass

# read a file and convert each line to set items
def fileToSet(fileName):
    result = set()
    with open(fileName, 'rt') as f:
        for line in f:
            result.add(line.replace('\n',''))
    return result

# interate through a set, each item will be a new line in the file
def setToFile(links, file):
    deleteFileContents(file)
    for link in sorted(links):
        appendToFile(file, link)
