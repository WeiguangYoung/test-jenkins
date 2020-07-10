import os
import uuid
import requests
import mimetypes

headers = {
    'TOKENID': "34e64f9290470989189f6b40a283fa6d538c34286a3aef2a2c2de4776b4c7329"
}


def upload_chunk(file_path, url):
    u_id = ''.join(str(uuid.uuid4()).split('-'))
    file_type, _ = mimetypes.guess_type(file_path)
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        i = 1
        while True:
            file_bytes = f.read(1024000)
            if not file_bytes:
                break
            file_data = {
                "file": file_bytes
            }
            form_data = {
                "resumableChunkNumber": i,
                "resumableIdentifier": u_id
            }
            requests.post(
                url=url, files=file_data, data=form_data, headers=headers
            )
            i += 1
    return [file_type, file_name, u_id, i - 1]


def merge_chunk(file_type, file_name, u_id, total_chunk, upload_type, url):
    file_list = [{
        'name': file_name,
        'type': file_type,
        'uid': u_id,
        'totalchunk': total_chunk
    }]
    form_data = {
        'type': upload_type,
        'filelist': str(file_list)
    }
    # form_data = json.dumps(form_data)
    print(form_data)
    response = requests.post(url, data=form_data, headers=headers)
    print(response.json())


if __name__ == '__main__':
    # url_1 = 'http://themis.konkii.com/api/files/upload'
    # test_file = '/home/konkii/Pictures/beach-dawn-dusk-ocean.jpg'
    # res = upload_chunk(test_file, url_1)
    #
    # url_2 = 'http://themis.konkii.com/api/files/merge'
    # merge_chunk(*res, 'background', url_2)
    with open("/home/konkii/dataset/test.txt") as f:
        file_data = f.read()
    url = "http://127.0.0.1:8003/api/v1/models/81/prediction/"
    res_data = requests.post(url, files={
        "data_binary": file_data
    })
    print(res_data.status_code)
    print(res_data.json())
