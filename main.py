import data_fetch as df

def start(subreddit : str,slimit : int,sreplace_limit :int):
    data = df.getComments(subreddit,slimit,sreplace_limit)
    print("DATA's Fetched Successfully")
    print(20*"-")
    df.json_convert(data[0],data[1])
    print("DATAS WERE CONVERTED SUCCESSFULLY")
    print(20*"-")
    print("ALL TASKS WERE COMPLETED")

def main():
    sreddit=input("Subreddit Name: ")
    slimit = int(input("Submission Search Limit: "))
    sreplace_limit = int(input("Comment Replace Limit:"))
    print("Starting...")
    print(20*"-")
    start(sreddit,slimit,sreplace_limit)

main()
