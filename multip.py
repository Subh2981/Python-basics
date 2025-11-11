import multiprocessing as ml
import requests as rs

def downloadfile(url,name):
    print("Started Downloading {name}")
    response =rs.get(url)
    open(f"files/{name}.jpg","wb").write(response.content)
    print("Finished Downloading {name}")


url="https://picsum.photos/200/300"
# for i in range(5):
#     #downloadfile(url,i)
#     pros=[]
#     p=ml.Process(target=downloadfile, args=[url,i])
#     p.start()
#     pros.append(p)
    
# for p in pros:
#     p.join()
    
if __name__ == "__main__": 
    ml.freeze_support()
    pros = []
    for i in range(5):
        p = ml.Process(target=downloadfile, args=(url, i))
        pros.append(p)
        p.start()

    for p in pros:
     p.join()