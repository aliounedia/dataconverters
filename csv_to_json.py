"""
This file demostrate how you can dowload a file using ressouces url.
IF we considere this dataset returned by the api.

{
        "author": "", 
        "author_email": "", 
        "ckan_url": "http://thedatahub.org/dataset/rep-re-statistiques-janvier-2012", 
        "download_url": "http://www.ansd.sn/publications/conjoncturelles/ReperStat/ReperStat_01_12.pdf", 
        "extras": {}, 
        "groups": [
            "country-sn"
        ], 
        "id": "b2e5ec1a-5818-4c89-8739-f6ece9d478cf", 
        "isopen": false, 
        "license": null, 
        "license_id": "", 
        "license_title": "", 
        "maintainer": "", 
        "maintainer_email": "", 
        "metadata_created": "2013-03-29T10:17:07.787491", 
        "metadata_modified": "2013-05-02T18:56:18.799290", 
        "name": "rep-re-statistiques-janvier-2012", 
        "notes": "", 
        "notes_rendered": "", 
        "ratings_average": null, 
        "ratings_count": 0, 
        "relationships": [], 
        "resources": [
            {
                "cache_last_updated": null, 
                "cache_url": "", 
                "created": "2013-03-29T05:17:07.948745", 
                "description": "", 
                "format": "", 
                "hash": "", 
                "id": "a621d33f-d18e-475d-9606-b1f2fc1e423a", 
                "last_modified": "2013-03-29T05:17:11.777571", 
                "mimetype": "application/pdf", 
                "mimetype_inner": "", 
                "name": "", 
                "package_id": "b2e5ec1a-5818-4c89-8739-f6ece9d478cf", 
                "position": 0, 
                "resource_group_id": "50c0f488-4ea4-4958-88f5-5fa71c3df992", 
                "resource_type": "file", 
                "size": "197902", 
                "tracking_summary": {
                    "recent": 0, 
                    "total": 0
                }, 
                "url": "http://www.ansd.sn/publications/conjoncturelles/ReperStat/ReperStat_01_12.pdf", 
                "webstore_last_updated": null, 
                "webstore_url": ""
            }, 
            {
                "cache_last_updated": null, 
                "cache_url": null, 
                "cache_url_updated": "2013-05-02T18:56:05", 
                "created": "2013-05-02T13:56:16.890972", 
                "description": "", 
                "format": "application/vnd.ms-excel", 
                "hash": "5acfa9652dfadecb129ddaf36e1120715919e84f", 
                "id": "a7da5582-fd8b-419d-8916-01cfd124939a", 
                "last_modified": "2013-05-02T13:56:18.635156", 
                "mimetype": "application/vnd.ms-excel", 
                "mimetype_inner": "", 
                "name": "2013-05-02T185247/Valeurs_ajoutees_par_branches_dactivites_aux_prix_constants_de_1999_en_milliards_FCFA).csv", 
                "owner": "f2aad7a3-0ad2-4ef9-8931-0277987525e9", 
                "package_id": "b2e5ec1a-5818-4c89-8739-f6ece9d478cf", 
                "position": 1, 
                "resource_group_id": "50c0f488-4ea4-4958-88f5-5fa71c3df992", 
                "resource_type": "file.upload", 
                "size": "506", 
                "tracking_summary": {
                    "recent": 0, 
                    "total": 0
                }, 
                "url": "https://ckannet-storage.commondatastorage.googleapis.com/2013-05-02T185247/Valeurs_ajoutees_par_branches_dactivites_aux_prix_constants_de_1999_en_milliards_FCFA).csv", 
                "webstore_last_updated": null, 
                "webstore_url": null
            }
        ], 
        "revision_id": "1544913a-8099-49a1-92ab-3d5d1e8dd239", 
        "state": "active", 
        "tags": [
            "ANSD", 
            "Senegal", 
            "donnees", 
            "menages", 
            "publications"
        ], 
        "title": "Rep\u00e8re Statistiques Janvier 2012", 
        "tracking_summary": {
            "recent": 0, 
            "total": 0
        }, 
        "type": null, 
        "url": "http://www.ansd.sn/publications/conjoncturelles/ReperStat/ReperStat_01_12.pdf", 
        "version": ""
    }
"""
import urllib
import dataconverters.jsondata as js
import dataconverters.commas as dcsv
def test_csv_from_ressource():
    """ download file from ressource """
    url  ="https://ckannet-storage.commondatastorage.googleapis.com/2013-05-02T185247/Valeurs_ajoutees_par_branches_dactivites_aux_prix_constants_de_1999_en_milliards_FCFA).csv"
    instream   =urllib.urlopen(url)
    records, metadata = dcsv.parse(instream,
                                guess_types=True
                                #guess_types=args.guess_types)
                                   )
    outstream = open("some_json.json", 'w')
    js.write(outstream, records, metadata)
if __name__ =="__main__":
    test_csv_from_ressource()
    
  
    
