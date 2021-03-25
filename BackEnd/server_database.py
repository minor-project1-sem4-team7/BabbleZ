#server side
#base model, needs to be developed
# it will be developed alongside coding of texting 



import pprint
import pymongo
import datetime

class server__database:
    def __init__(self):
        self.myclient= pymongo.MongoClient("mongodb://localhost:27017/") #connect to the cloud database 
        self.mydb=self.myclient['server_database']

    
    def update_client_socket(self,socket):
        pass


# still have to set the counter to no. of the messages corresponding to a particular collection 
    def update_counter(self):
        pass



    def create_database(self,basic_info): #basic_info is a dictionary containing basic info of the client 
       
        
        
        #creating the database
        print("hey how are you")

        collist=self.mydb.list_collection_names()

        
        self.coll=self.mydb[basic_info['userid']]

        if basic_info['userid'] not in collist: 

            document={'username':basic_info['username'],'password':basic_info['password'],'public_key':basic_info['public_key'],'app_key':basic_info['app_key']
                    ,'client_socket':basic_info['client_socket'], 'messages':[] }
            
            self.coll.insert_one(document)


        print(self.mydb.list_collection_names())

        for x in self.coll.find():
            pprint.pprint(x)

        # self.coll.insert_one(document)

        # self.coll.insert_one(basic_info['client_socket'])
        # self.coll.insert_one("messages":{})


        # self.mydb=self.myclient[basic_info['name']]
        # self.coll=self.mydb[recv_name]
        # self.coll.insert_one({"messages":{}})




    def load_msg(self,msg,recv_id):
        #can improve the timestamp process 
        # pass 
        collist=self.mydb.list_collection_names()
        if recv_id in collist:
            print('hey how are you lol')
            self.coll=self.mydb[recv_id]
            doc=self.coll.find_one({'userid':recv_id})
            doc.messages.append(msg)
            # self.coll.messages.insert_one(msg)

            for x in self.coll.find():
                print(x)

        else:
            print("not found")

        

        # self.coll=self.mydb[recv_name]
        # timestamp=datetime.datetime.now()
        # doc={"message":msg,"timestamp":timestamp}
        # x=self.coll.messages.insert_one(doc)



