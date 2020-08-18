import __main__
import fileinput
import re


def get_version_unix(project_type):
    retrieve_ver_command = ''
    retrieve_ver_command2 = ''
    ## check type of project
    if project_type == 'npm':
        retrieve_ver_command  = "grep 'version\s*:\s*' package.json"
    if project_type == 'java':
        retrieve_ver_command = "grep 'version"
    if project_type == 'android':
        retrieve_ver_command1 = "grep 'versionCode\s*' app/build.gradle"
        retrieve_ver_command2 = "grep 'versionName\s*' app/build.gradle"
    if project_type == 'flutter':
        retrieve_ver_command = "grep 'version\s*:\s*' pubspec.yaml"
    if project_type == 'dotnet':
        retrieve_ver_command = ''
    if project_type == 'netcore':
        retrieve_ver_command = ''  
            
def get_version(filename):
    result = 1
    version_string = ''
    
    versionstr = ''
    if __main__.debug == 1:
        print("File searched for version number: ", filename)
    if __main__.os.path.exists(filename):
        with open(filename) as origin_file:
            for line in origin_file:
                if re.search(r'version', line):
                    result = 0
                    versionstr = line
    else:
        print("Could not find file with version number")
        return __main__.sys.exit(2)

    if __main__.arch_type == 'npm':
        print("Architecture::: Typescript/Javascript: NPM build")
        strip_version = versionstr.strip()
        split_version = strip_version.split(":")
        version_string = re.sub('[,"]', '', split_version[1])   
        version_string = version_string.strip() 
            
    elif __main__.arch_type == 'gradle':
        print("Architecture::: Java : Gradle build")
        strip_version = versionstr.strip()
        split_version = strip_version.split("=")
        version_string = re.sub("[']", '', split_version[1].strip())
        
        
    elif __main__.arch_type == 'flutter':
        print("Architecture::: Flutter")
        strip_version = versionstr.strip()
        split_version = strip_version.split("+")
        versionCode, versionName = split_version
        versionCode = re.sub("[']", '', versionCode.strip())
        versionName = re.sub("[']", '', versionName.strip())
    
    elif __main__.arch_type == 'maven':
        print("Architecture::: Java : Maven build")
        strip_version = versionstr.strip()
        version_string = re.sub('<[^<]+>', '', strip_version)
        version_string = version_string.strip()
             
    elif __main__.arch_type == 'dotnet':
        print("Architecture::: .NET/C# : MSbuild")
        strip_version = versionstr.strip()
        version_string = re.sub('<[^<]+>', '', strip_version)
        version_string = version_string.strip()
        
    elif __main__.arch_type == 'netcore':
        print("Architecture::: .NetCore/C# ")
        strip_version = versionstr.strip()
        version_string = re.sub('<[^<]+>', '', strip_version)
        version_string = version_string.strip()
    
    return version_string    

def process_version(versionstr):
    major = 0
    minor = 0
    patch = 0 
    build = 0
    
    current_version = ''
    prelease_version = ''
    version_lst = []
    new_version = ''
    
    if versionstr == '':
        print("No version number detected.")
        return __main__.sys.exit(2)    
    # Semantic version standard A pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers 
    # immediately following the patch version.
    check_prerelease = versionstr.split("-") 
    if len(check_prerelease) == 1:
        current_version = check_prerelease[0]
    else:
        current_version = check_prerelease[0]
        prelease_version = check_prerelease[1]
            
            
    version_lst = current_version.split(".")
    
    if (len(version_lst) == 4):
        version_format = "modified"
        major, minor, patch, build = version_lst
    else:
        version_format = "standard"
        major, minor, patch = version_lst
            
    if __main__.change_type == "major":
        major = int(major) + 1
        if version_format == "standard":
            minor = 0
            patch = 0
        else:
            minor = 0
            patch = 0
            build = 0         
            
    if __main__.change_type == "minor":    
        minor = int(minor) + 1  
        patch = 0
        if version_format != "standard":
            build = 0
    
    if __main__.change_type == "patch":
        patch = int(patch) + 1
        if version_format != "standard":
            build = 0
    
    if __main__.change_type == "build":
        build = int(build) + 1    
    
    if version_format == "standard":
        new_version = str(major) + '.' + str(minor) + '.' + str(patch)
    else:
        new_version = str(major) + '.' + str(minor) + '.' + str(patch) + '.' + str(build)
        
    if prelease_version != '' and __main__.change_type == 'prerelease':
        new_version = new_version + '-' + prelease_version
                    
    return new_version      
        
         
            
        
def replace_version(filename, search_text, replacement_text):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(search_text, replacement_text), end='')  
            
def change_version_file(filepath, version, newversion):
    path = __main__.os.path.abspath(__main__.os.getcwd()) 
    if __main__.debug == 1:
        print("Old version: ", version)
        print("New version: ", newversion)
        print("File path: ", filepath)
    old_version = ''
    new_version = ''
    
    if __main__.arch_type == 'npm':
        old_version = "\"version\": \"{}\",".format(version)
        new_version = "\"version\": \"{}\",".format(newversion)
        replace_version(filepath, old_version, new_version)
        
    if __main__.arch_type == 'flutter':
        old_version = "version: {}".format(version)
        new_version = "version: {}".format(newversion)
        replace_version(filepath, old_version, new_version)  
        
    if __main__.arch_type == 'gradle':
        java_android_build_file = __main__.os.path.join(path, 'app/build.gradle')
        if __main__.os.path.exists(java_android_build_file):
            test = 1
            ## update versionCode and versionName
        else:
            old_version = "version = '{}'".format(version)
            new_version = "version = '{}'".format(newversion)
            replace_version(filepath, old_version, new_version)        
            
    if __main__.arch_type == 'dotnet':
        old_version = "<AssemblyVersion>{}</AssemblyVersion>".format(version)
        new_version = "<AssemblyVersion>{}</AssemblyVersion>".format(newversion)
        replace_version(filepath, old_version, new_version)        
    
    if __main__.arch_type == 'netcore':
        old_version = "<AssemblyVersion>{}</AssemblyVersion>".format(version)
        new_version = "<AssemblyVersion>{}</AssemblyVersion>".format(newversion)
        replace_version(filepath, old_version, new_version)      
         
def change_manifest(v, dv):
    ## Retreive version number manifest
    ## grep "version\s*=\s*" manifest.yml  ## To-do Refactor to use this 
    
    path = __main__.os.path.abspath(__main__.os.getcwd()) 
    file_path = __main__.os.path.join(path, 'manifest.yml')
    
    old_version = "version: {}".format(v)
    new_version = "version: {}".format(dv)
    replace_version(file_path, old_version, new_version)
    
    
    ## check if manifest.yml exist
    ## sed_command_manifest = "sed -i 's/version: {}/version: {}/g' ./manifest.yml".format(v.rstrip(), dv)
 
    ## update version number in manifest.yml
    ##process_sed_manifest = __main__.Popen(sed_command_manifest, shell=True, stdout=__main__.PIPE, cwd=path)

def modify_version():

        
    new_version = ''
    curr_version = ''
    version_format = ''
    version_file = ''

    path = __main__.os.path.abspath(__main__.os.getcwd())    
    if __main__.debug == 1:
        print("Working directory: ",path)
    
    search_ver_text = ''
    
    git_checkout_command = "git checkout -b feature/modify-version"
    process_checkout_command = __main__.Popen(git_checkout_command, shell=True, stdout=__main__.PIPE, cwd=path)
    print("Checkout result: ", process_checkout_command.communicate()[0])
    
    if __main__.arch_type == 'npm':
        version_file = 'package.json'
        search_ver_text = "\"version\": v" 
        
    if __main__.arch_type == 'flutter':
        version_file = 'pubspec.yaml'
        ## updaet version code and name
        
    if __main__.arch_type == 'gradle':
        java_android_build_file = __main__.os.path.join(path, 'app/build.gradle')
        if __main__.os.path.exists(java_android_build_file):
            version_file = 'app/build.gradle'
            ## update versionCode and versionName
        else:
            version_file = 'build.gradle'
            
    if __main__.arch_type == 'dotnet':
        version_file = ''
    
    if __main__.arch_type == 'netcore':
        version_file = ''
   
    
    filepath = __main__.os.path.join(path, version_file)
    curr_version = get_version(filepath)
    if __main__.debug == 1:
        print("Current version: ", curr_version)
    new_version = process_version(curr_version)

    change_manifest(curr_version, new_version)  ## Update manifest file
    change_version_file(filepath, curr_version, new_version)
    
   
    ##replace_version(filepath, )

    print("Previous version: ", curr_version, "  New Version:: ", new_version, "   Type: ", __main__.change_type)
    
    return __main__.sys.exit(0)
  