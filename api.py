"""
    Colectica API
"""

import requests
import json


# item type dictionary
#   See Item Type Identifiers for a list of identifiers for all item types.
#   https://docs.colectica.com/repository/technical/item-type-identifiers/
item_dict = {
  "Action": "0b70f0ba-602a-4575-a15c-91f0915bae36",
  "Archive": "ae8ee886-70a2-4c30-a879-b7d92605ba68",
  "Category": "7e47c269-bcab-40f7-a778-af7bbc4e3d00",
  "Category Group": "8a3ba89d-70da-4ba1-871a-b41954175453",
  "Category Set": "1c11de94-a36d-4d80-95dc-950c6f37f624",
  "ClassificationCorrespondenceTable": "D55A2705-0AB6-464F-92DD-8E78D10269D8",
  "ClassificationFamily": "020B8B81-2CCD-4F1D-85BA-F724CE1724AC",
  "ClassificationIndex": "F2C1F48C-A119-4576-9475-607E8E8A8A12",
  "ClassificationItem": "E96C1674-C4D9-450A-877A-BD37C3060526",
  "ClassificationLevel": "EF15C75E-FABA-4192-8FB0-19CF7A3436DB",
  "ClassificationSeries": "3844452A-F213-4296-845A-2FC00835F97A",
  "Code List Group": "394b9ff3-7248-4ede-b945-9bebdbf56bed",
  "Code List Set": "4193d389-b5ae-4368-b399-cd5a7ee3653c",
  "Code Set": "8b108ef8-b642-4484-9c49-f88e4bf7cf1d",
  "Concept": "48b7d4b4-72bf-470a-a885-720f89bfbc40",
  "Concept Group": "d38bfe75-60a9-460a-affa-61d643b5416b",
  "Concept Set": "63c9f58d-1ea3-4239-99cf-e4418ec384c5",
  "Conceptual Component": "d747d7db-ed2a-4339-a156-127f8786d5ec",
  "Conceptual Variable": "75f63016-b4f8-45b6-953c-f7ac7364fc25",
  "Conceptual Variable Group": "dceb4eb2-e7bb-46f8-804d-d9a86aa5ee9f",
  "Conceptual Variable Set": "ce0f8af6-db9c-4fb3-a31a-e9523fc53668",
  "Conditional": "2af9a279-89ee-4d06-b2d2-54563a6946ea",
  "Control Construct Group": "6bcbb890-751d-41e5-a0c9-27d5c951cf93",
  "Control Construct Set": "ed3801fe-6798-4ea6-808b-73052cc1c633",
  "Data Collection": "c5084916-9936-47a9-a523-93be9fd816d8",
  "Data File": "a51e85bb-6259-4488-8df2-f08cb43485f8",
  "Data Layout": "f39ff278-8500-45fe-a850-3906da2d242b",
  "DataCollection Methodology": "aa80eb80-c5a9-4215-a59f-4862c6b4009f",
  "General Instruction": "723052be-35ac-4e63-84c6-743a0a693d85",
  "Generation Instruction": "eca6afce-0840-421a-beae-d3283fae32b1",
  "Individual": "1DD920A2-DED8-48B8-B085-D62E49DFC627",
  "Instruction Group": "89688a09-e125-4b62-997e-18a14df90578",
  "Instrument": "f196cc07-9c99-4725-ad55-5b34f479cf7d",
  "Instrument Group": "27540e4f-9a3a-415e-8fb9-83c095dc7bcb",
  "Instrument Set": "f152ee61-08ba-4fca-8a3a-daf8f87f972e",
  "Interviewer Instruction": "f53f37b2-6f1b-4af3-b89a-4909d512dfb2",
  "Interviewer Instruction Set": "5bf598a9-9333-4c84-8c10-46195776800a",
  "Logical Product": "965c8d28-7d48-4950-bea7-04b27e52bb9b",
  "Loop": "7482a1bf-fea5-4955-9fc0-f76c053e5b2d",
  "Managed Representation Group": "68cac1f8-a2a6-49a7-9402-58b8df3d1921",
  "Managed Representation Set": "16d4d829-41e1-4677-aa17-81190b6a0e66",
  "MeasurementItem": "CF6FA3D8-3297-42D5-8922-0BA2D4B5C9FF",
  "MeasurementConstruct": "44CB69AC-062C-4EC2-970B-AF73B42D3CB8",
  "Metadata Package": "679a61f5-4246-4c89-b482-924dec09af98",
  "NCube": "b771f5fd-3b29-4f4d-a4f5-6ccae1138c89",
  "NCube Group": "47172a68-4b16-4f3b-b484-daace3f45bcc",
  "NCube Set": "31e8515b-c0cc-4e88-9e00-ae4bb6d4ac25",
  "Organization": "be33a54f-ca93-454f-9164-8c41df6212cb",
  "Organization Group": "28455ff2-d6a9-4aa3-9c9f-f6b22b55b3a8",
  "Organization Set": "08ed326a-8043-4da2-ace9-3f5bd19b6196",
  "OtherMaterial": "EACCE1D3-011D-4980-BD4D-6CCFB9161B43",
  "OtherMaterialGroup": "E24AFC19-5618-4050-84C7-1A464AF88485",
  "OtherMaterialScheme": "D19C0898-743A-4AAC-A0ED-7BDF979E5957",
  "Physical Data Product": "e27aac79-be4a-47d3-96e3-36da178f3923",
  "Physical Structure": "b89d26c3-c9e1-4720-a6e4-3a1d8cdb10ce",
  "PhysicalStructure Set": "19273b86-934a-4c2c-9b64-bd2b3bb07acd",
  "Processing Event": "e99acc19-d127-413d-9cf9-aed786e62055",
  "Processing Event Group": "a64a0ab6-5bfa-43dd-a3fb-e791f8f28c58",
  "Processing Event Set": "dc15c74b-9b4a-492e-9ddd-4e02eca9d9d7",
  "Processing Instruction Group": "c49e2c65-52fb-4948-a454-f3431b834fe7",
  "Processing Instruction Scheme": "a1a5c54a-3a7b-4dfb-a5fa-46ed8ef465cc",
  "Project": "f2b9352a-d976-4eac-8ee1-0c76da7cfca4",
  "Quality Standard": "711e9487-82fd-4682-9309-22e1272bab2c",
  "Quality Statement": "831a2d3f-7649-485d-90a4-359e2591e1df",
  "Quality Statement Group": "a60d1016-3d44-4182-bbf7-a5812d817f71",
  "Quality Statement Set": "4aa7ea9c-495d-4919-95f7-ac107c877f56",
  "Question": "a1bb19bd-a24a-4443-8728-a6ad80eb42b8",
  "Question Activity": "f433e43d-29a4-4c25-9610-9dd9819a0519",
  "Question Block": "12d8f742-0433-4f12-88d1-eb9b77ceced5",
  "Question Grid": "a1b8a30e-2f35-4056-8467-40e7ed0e7379",
  "Question Group": "5cc915a1-23c9-4487-9613-779c62f8c205",
  "Question Set": "0a63fcf6-ffdd-4214-b38c-147d6689d6a1",
  "RecordLayout": "faddcfca-bedd-450f-9b4e-15c3f2458713",
  "RecordLayout Set": "8e4d59db-e757-4e94-bb19-1ac72761566e",
  "Repeat": "3a4e92c0-fd99-4d3f-9b66-471674ab7670",
  "Represented Variable": "1044459c-8ae2-474a-ad96-6ec18b04953c",
  "Represented Variable Group": "a8cecef5-4493-47b8-9c83-82a2f1cfb08e",
  "Represented Variable Set": "14404696-2db3-45ac-a94d-139521de6e21",
  "Reusable Missing Value": "c29c3125-2a53-4179-8fa6-aa3beb2bb5ed",
  "Sequence": "df457731-a75c-47c3-aeb4-7969d55aa049",
  "Series": "4bd6eef6-99df-40e6-9b11-5b8f64e5cb23",
  "Statement": "4a8b1d85-a508-4b4f-8d56-798219f59689",
  "StatisticalClassification": "9BACF643-4EF3-452B-8074-D12EE2404704",
  "Study": "30ea0200-7121-4f01-8d21-a931a182b86d",
  "SubSeries": "2d57296d-095c-485a-b970-8c63c215c1d0",
  "UnitType": "897D4AA9-0C26-490B-B25E-F29D9FF721A5",
  "UnitTypeScheme": "32E1427F-0B88-4FE5-9F2D-5D3EAF585EE8",
  "UnitTypeGroup": "2B0A0A33-D233-40A3-993B-7CEDA290BC8D",
  "Universe": "66dfcb67-4915-41ae-9b13-c8ebff6d8e00",
  "Universe Group": "a80ecd09-7d81-4512-80bb-cdb60f9a95bf",
  "Universe Set": "101f901a-2c28-4931-88d6-8f80b36d5650",
  "Variable": "683889c6-f74b-4d5e-92ed-908c0a42bb2d",
  "Variable Group": "91da6c62-c2c2-4173-8958-22c518d1d40d",
  "Variable Set": "50907716-b67a-4dcd-8f9f-8a283cb5fee0",
  "Variable Statistic": "3b438f9f-e039-4eac-a06d-3fa1aedf48bb",
  "While": "0681e606-ba3f-453c-9fdd-10670e8e045c"
}

item_dict_inv = {v:k for k,v in item_dict.items()} 


def get_jwtToken(hostname, username, password):
    """
        First obtain a JWT access token
        documented at https://docs.colectica.com/portal/technical/deployment/local-jwt-provider/#usage
    """
    tokenEndpoint = "https://" + hostname + "/token/createtoken"
    response = requests.post(tokenEndpoint, json={'username': username, 'password': password}, allow_redirects=True, verify=False)

    if response.ok is not True:
        print("Could not get token. Status code: ", response.status_code)
        quit()

    jsonResponse = response.json()
    jwtToken = jsonResponse["access_token"]
    tokenHeader = {'Authorization': 'Bearer ' + jwtToken}

    # get Repository information
    #response = requests.get("https://"+self.host+"/api/v1/repository/info", headers=tokenHeader, verify=False)
    return tokenHeader


class ColecticaLowLevelAPI():
    """Acts as a frontend to a Colectica portal.

    You can then make API calls to this.  It caches authentication credentials, etc.
    """
    def __init__(self, hostname, username, password):
        self.host = hostname
        self.token = get_jwtToken(hostname, username, password)


    def item_code(self, item):
        return item_dict[item]


    def item_code_inv(self, item_type_id):
        return item_dict_inv[item_type_id]

        
    def get_an_item(self, AgencyId, Identifier):
        """
        This request retrieves the lastest version of an item based on known identification information.
        https://docs.colectica.com/portal/api/examples/get-item/
        Request Type: GET
        URL: /api/v1/item/agenct/Id
        """
        response = requests.get("https://"+self.host+"/api/v1/item/"+AgencyId+"/"+Identifier, headers=self.token, verify=False)
        if response.ok:
            if response.json() != []:
                return response.json()


    def general_search(self, item_type, search_term, MaxResults=1, RankResults=True, SearchDepricatedItems=False, SearchLatestVersion=True):
        """
            Perform a general search: https://docs.colectica.com/portal/api/examples/search/
            Request Type: POST
            URL: /api/v1/_query
        """
        # MaxResults=0 returns all results
        jsonquery =  {
             "Cultures": [
                 "en-US"
             ],
             "ItemTypes": [
                 item_type
             ],
             "LanguageSortOrder": [
                 "en-US"
             ],
             "MaxResults": MaxResults,
             "RankResults": RankResults,
             "ResultOffset": 0,
             "ResultOrdering": "None",
             "SearchDepricatedItems": SearchDepricatedItems,
             "SearchTerms": [
                 search_term
             ],
             "SearchLatestVersion": SearchLatestVersion
         }

        response = requests.post("https://"+self.host+"/api/v1/_query/", headers=self.token, json=jsonquery, verify=False)
        if response.ok:
            return response.json()




    def relationship_search(self, item_type, AgencyId, Identifier, UseDistinctResultItem=True, UseDistinctTargetItem=True):
        """
            Option 1: retrieve identifiers only
            https://docs.colectica.com/portal/api/examples/relationship-search/
            Request Type: POST
            URL: /api/v1/_query/relationship/bysubject
        """

        jsonquery = {
             "ItemTypes": [
                 item_type
             ],
             "TargetItem": {
                 "AgencyId": AgencyId,
                 "Identifier": Identifier,
                 "Version": 1
             },
             "UseDistinctResultItem": UseDistinctResultItem,
             "UseDistinctTargetItem": UseDistinctTargetItem
        }

        response = requests.post("https://"+self.host+"/api/v1/_query/relationship/bysubject/", headers=self.token, json=jsonquery, verify=False)
        if response.ok:
            if response.json() != []:
                return(response.json())


    def get_an_item_version(self, AgencyId, Identifier, Version):
        """
            This request an item based on known identification information.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1ItemByAgencyByIdByVersionGet
            Request Type: GET
            URL: /api/v1/item/{agency}/{id}/{version}
        """
        response = requests.get("https://"+self.host+"/api/v1/item/"+AgencyId+"/"+Identifier+"/"+Version, headers=self.token, verify=False)
        if response.ok:
            if response.json() != []:
                return response.json()


    def get_item_version_history(self, AgencyId, Identifier):
        """
            Gets the version history of an item.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1ItemByAgencyByIdHistoryGet
            Request Type: GET
            URL: /api/v1/item/{agency}/{id}/history
        """
        response = requests.get("https://"+self.host+"/api/v1/item/"+AgencyId+"/"+Identifier+"/history", headers=self.token, verify=False)
        if response.ok:
            if response.json() != []:
                return response.json()

    def colectica_get_api(self, url, hostname, tokenHeader):
        """
            Gets the version history of an item.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1ItemByAgencyByIdHistoryGet
            Request Type: GET
            URL: /api/v1/item/{agency}/{id}/history
        """
        response = requests.get("https://"+self.host+"/api/v1/"+url, headers=self.token, verify=False)
        if response.ok:
            if response.json() != []:
                return response.json()

    def get_item_description(self, AgencyId, Identifier, Version):
        """
            Gets a description of a repository item. The description contains identification, naming, 
            and summary information, but not the entire contents of the item.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1ItemByAgencyByIdByVersionDescriptionGet
            Request Type: GET
            URL: /api/v1/item/{agency}/{id}/{version}/description
        """
        response = requests.get("https://"+self.host+"/api/v1/item/"+AgencyId+"/"+Identifier+"/"+Version+"/description", headers=self.token, verify=False)
        if response.ok:
            if response.json() != []:
                return response.json()


    def relationship_bysubject_descriptions(self, item_type, AgencyId, Identifier, Version, UseDistinctResultItem=True, UseDistinctTargetItem=True):
        """
            Gets the repository item descriptions for items that match the specified relationship search parameters. 
            The search will query for items referenced by the target item specified in the search facet.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1_queryRelationshipBysubjectDescriptionsPost
            Request Type: POST
            URL: /api/v1/_query/relationship/bysubject/descriptions
        """

        jsonquery = {
             "ItemTypes": [
                 item_type
             ],
             "TargetItem": {
                 "AgencyId": AgencyId,
                 "Identifier": Identifier,
                 "Version": Version
             },
             "UseDistinctResultItem": UseDistinctResultItem,
             "UseDistinctTargetItem": UseDistinctTargetItem
        }

        response = requests.post("https://"+self.host+"/api/v1/_query/relationship/bysubject/descriptions", headers=self.token, json=jsonquery, verify=False)
        if response.ok:
            if response.json() != []:
                return(response.json())


    def relationship_byobject_descriptions(self, item_type, AgencyId, Identifier, Version, UseDistinctResultItem=True, UseDistinctTargetItem=True):
        """
            Gets the repository item descriptions for items that match the specified relationship search parameters. 
            The search will query for items that reference the target item specified in the search facet.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1_queryRelationshipByobjectDescriptionsPost
            Request Type: POST
            URL: /api/v1/_query/relationship/byobject/descriptions
        """

        jsonquery = {
             "ItemTypes": [
                 item_type
             ],
             "TargetItem": {
                 "AgencyId": AgencyId,
                 "Identifier": Identifier,
                 "Version": Version
             },
             "UseDistinctResultItem": UseDistinctResultItem,
             "UseDistinctTargetItem": UseDistinctTargetItem
        }

        response = requests.post("https://"+self.host+"/api/v1/_query/relationship/bysubject/descriptions", headers=self.token, json=jsonquery, verify=False)
        if response.ok:
            if response.json() != []:
                return(response.json())


    def relationship_bysubject(self, item_type, AgencyId, Identifier, Version,  UseDistinctResultItem=True, UseDistinctTargetItem=True):
        """
            Gets a list of items referenced by the specified item, according to the provided search options.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1_queryRelationshipBysubjectPost
            Request Type: POST
            URL: /api/v1/_query/relationship/bysubject
        """

        jsonquery = {
             "ItemTypes": [
                 item_type
             ],
             "TargetItem": {
                 "AgencyId": AgencyId,
                 "Identifier": Identifier,
                 "Version": Version
             },
             "UseDistinctResultItem": UseDistinctResultItem,
             "UseDistinctTargetItem": UseDistinctTargetItem
        }

        response = requests.post("https://"+self.host+"/api/v1/_query/relationship/bysubject", headers=self.token, json=jsonquery, verify=False)
        if response.ok:
            if response.json() != []:
                return(response.json())


    def relationship_byobject(self, item_type, AgencyId, Identifier, Version, UseDistinctResultItem=True, UseDistinctTargetItem=True):
        """
            Gets a list of items that reference the specified item, according to the provided search options.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1_queryRelationshipByobjectPost
            Request Type: POST
            URL: /api/v1/_query/relationship/byobject
        """

        jsonquery = {
             "ItemTypes": [
                 item_type
             ],
             "TargetItem": {
                 "AgencyId": AgencyId,
                 "Identifier": Identifier,
                 "Version": Version
             },
             "UseDistinctResultItem": UseDistinctResultItem,
             "UseDistinctTargetItem": UseDistinctTargetItem
        }

        response = requests.post("https://"+self.host+"/api/v1/_query/relationship/bysubject", headers=self.token, json=jsonquery, verify=False)
        if response.ok:
            if response.json() != []:
                return(response.json())


    def relationship_matrix(self, AgencyId, Identifier, Version, Predicate, ReverseTraversal=True):
        """
            Gets a matrix representing all items in a set and the relationships among those items.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1_queryRelationshipMatrixPost
            Request Type: POST
            URL: /api/v1/_query/relationship/matrix
        """

        jsonquery = {
            "RootItems": [
                {
                "AgencyId": AgencyId,
                "Identifier": Identifier,
                "Version": Version
                }
            ],
            "Facet": {
                "Predicate": Predicate,
                "ReverseTraversal": ReverseTraversal
            }
        }

        response = requests.post("https://"+self.host+"/api/v1/_query/relationship/matrix", headers=self.token, json=jsonquery, verify=False)
        if response.ok:
            if response.json() != []:
                return(response.json())


    def relationship_matrix_typed(self, AgencyId, Identifier, Version, Predicate, ReverseTraversal=True):
        """
            Gets a matrix representing all items in a set and the relationships among those items.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1_queryRelationshipMatrixPost
            Request Type: POST
            URL: /api/v1/_query/relationship/matrix/typed
        """

        jsonquery = {
            "RootItems": [
                {
                "AgencyId": AgencyId,
                "Identifier": Identifier,
                "Version": Version
                }
            ],
            "Facet": {
                "Predicate": Predicate,
                "ReverseTraversal": ReverseTraversal
            }
        }

        response = requests.post("https://"+self.host+"/api/v1/_query/relationship/matrix/typed", headers=self.token, json=jsonquery, verify=False)
        if response.ok:
            if response.json() != []:
                return(response.json())


    def get_a_set(self, AgencyId, Identifier, Version):
        """Gets the set of all items under the specified root.

        Frontend to Colectica GET: /api/v1/set/{agency}/{id}/{version}

        Args:
            AgencyId (str):  foo foo foo
            Identifier (str):
            Version (str): 
            hostname (str):
            tokenHeader (str): 

        Returns:
            dict: as documented at [1].

        [1] https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1SetByAgencyByIdByVersionGet
        """

        response = requests.get("https://" + self.host + "/api/v1/set/" + AgencyId + "/" + Identifier + "/" + Version , headers=self.token, verify=False)
        if response.ok:
            if response.json() != []:
                return response.json()


    def get_a_set_typed(self, AgencyId, Identifier, Version):
        """
            Gets the set of items defined by the specified root. Each item in the set will have the latest version number for that item.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1SetByAgencyByIdByVersionTypedGet
            Request Type: GET
            URL: /api/v1/set/{agency}/{id}/{version}/typed
        """

        response = requests.get("https://" + self.host + "/api/v1/set/" + AgencyId + "/" + Identifier + "/" + Version + "/typed", headers=self.token, verify=False)
        if response.ok:
            if response.json() != []:
                return response.json()


    def get_a_set_lasted(self, AgencyId, Identifier):
        """
            Gets the set of items defined by the specified root. Each item in the set will have the latest version number for that item.
            https://docs.colectica.com/portal/technical/api/v1/#operation/ApiV1SetByAgencyByIdGet
            Request Type: GET
            URL: /api/v1/set/{agency}/{id}
        """

        response = requests.get("https://" + self.host + "/api/v1/set/" + AgencyId + "/" + Identifier, headers=self.token, verify=False)
        if response.ok:
            if response.json() != []:
                return response.json()


if __name__ == "__main__":
    raise RuntimeError("don't run this directly")

