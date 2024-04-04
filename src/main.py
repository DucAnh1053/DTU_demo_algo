import pandas as pd
# import torch
import scipy.sparse as sparse
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# import calculate_IFF, estimate_IRT_params
from ..config import config 

# Initial Mongo Atlas Client | chuyển thành function
username = 'admin'
password ='admin123'
uri = f'mongodb+srv://{username}:{password}@cluster0.jmil5cr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0' # cái này đẩy vào configure
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Query dữ liệu từ Mongo | chuyển thành function
db = client['dtu']
playersCollection = db['players']
questionsCollection = db['questions']
resultCollection = db['answered_questions']

iterable_list = [1,2,3]
pipline_list = generate_monogo_template(r"D:\DuyTan_algorithm_demo\config\result_template.json",
                         [1,2,3])
# Pull dữ liệu từ Atlas
for pipeline in pipline_list:
    playerDataObject = playersCollection.aggregate(pipeline)
    for batch in playerDataObject:
    # Process each batch of data
    # player_ids = batch["player_id"]
    # # player_degree
    # questions_lists = batch["questions"]
    
    # print(f"Processing batch for player IDs: {player_ids}")
    # print(f"Questions lists: {questions_lists}")
    
        print(batch)
    # Optionally, clear batch from memory
    # del batch
# player_df = pd.DataFrame(list(players_data))



'''
#TODO
thêm tính toán bằng CUDA

dữ liệu đi vào
    mongo query
gọi 2 function để tính

trả về dữ liệu cho từng Player_ID
lưu vào database
'''
