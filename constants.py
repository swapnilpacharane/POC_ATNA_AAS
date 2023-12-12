import os
end_user= 'Adidas Singapore Pte Ltd'
# MongoDB_URL = "mongodb://mongoRootAdmin:mongoRootAdmin@atl-az-we-tis-dw-dev-shard-00-00.seiqd.mongodb.net:27017,atl-az-we-tis-dw-dev-shard-00-01.seiqd.mongodb.net:27017,atl-az-we-tis-dw-dev-shard-00-02.seiqd.mongodb.net:27017/?ssl=true&replicaSet=atlas-31rrlc-shard-0&authSource=admin&retryWrites=true&w=majority"
MongoDB_URL = "mongodb://192.168.115.123:27017/"
storage_account_name = "sdidwcheckpointuat"
container_name = "checkpoint-workbooks"
AccountKey = "54X3EJGbzAt9r7Xp16SSViAlCBsNXXm2vgDOZ7Cg8DIiAjGwlXSDJvRY4o9Mr8Oeo52dGlx5Ewv9+AStD9ZcDA=="
connect_str = "DefaultEndpointsProtocol=https;AccountName="+storage_account_name+";AccountKey="+AccountKey+";EndpointSuffix=core.windows.net"
path = os.path.join(os.getcwd(), 'TESTING.xls')
product_list_path = os.path.join(os.getcwd(), 'Product_List.xlsx')
dest_overview = os.path.join(os.getcwd(), 'TESTING_overview.xlsx')
dest_product = os.path.join(os.getcwd(), 'TESTING_product.xlsx')
dest_standalone = os.path.join(os.getcwd(), 'TESTING_standalone.xlsx')
dest_support = os.path.join(os.getcwd(), 'TESTING_support.xlsx')
username = "admin"
password = "Admin123"
# host = "emr.dev.splat.nttltd.global.ntt"
host = "192.168.115.123"
virtual_host = "MSP"
aas_exchange = "AAS"
publish_queue_tester = "AAS.RESPONSE.INBOUND.SDI_ASSET_ANALYTICS_DISCOVERY"
consume_queue_tester = "aas_request_outbound_aa_discovery"

