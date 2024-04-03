import multiprocessing

def run_script(script_name):
    exec(open(script_name).read())

if __name__ == "__main__":
    processes = []

    # 각각의 스크립트 파일을 실행할 프로세스를 생성합니다.
    path = 'C:/Users/User/OneDrive/바탕 화면/workspace/gentrification/gentrification/'
    scripts = [path+"a.py", path+"./b.py", path+"./c.py"]
    for script in scripts:
        process = multiprocessing.Process(target=run_script, args=(script,))
        processes.append(process)

    # 생성된 모든 프로세스를 시작합니다.
    for process in processes:
        process.start()

    # 모든 프로세스가 종료될 때까지 기다립니다.
    for process in processes:
        process.join()  