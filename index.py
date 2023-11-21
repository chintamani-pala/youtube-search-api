from flask import Flask, request, jsonify
from jinja2 import escape as jinja2_escape
from urllib.parse import quote as url_quote
from itsdangerous import json
from jinja2 import escape
import requests
import re
#import json

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({'credit': 'chintamani pala','portfolio':'chintamanipala.me'})


@app.route('/get', methods=['GET'])
def get_video_data():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'URL parameter missing'})
    url=f'https://www.youtube.com/results?search_query={query}'
    response = requests.get(url)
    pattern = re.compile(r'var ytInitialData = (.*?);</script>', re.DOTALL)
    matches = pattern.findall(response.text)
    base_url="https://youtube.com/watch?v="
    for match in matches:
        json_data = json.loads(match)
        if 'contents' in json_data:
            contents_value = json_data['contents']
            if 'twoColumnSearchResultsRenderer' in contents_value:
                two_column = contents_value['twoColumnSearchResultsRenderer']
                if 'primaryContents' in two_column:
                    primary_contents = two_column['primaryContents']
                    if 'sectionListRenderer' in primary_contents:
                        section_list_renderer = primary_contents['sectionListRenderer']
                        if 'contents' in section_list_renderer:
                            contents_list = section_list_renderer['contents']
                            if contents_list and isinstance(contents_list[0], dict):
                                item_section = contents_list[0].get('itemSectionRenderer', {})
                                extracted_value = item_section.get('contents', [])
                                final_array = []
                                for item in extracted_value:
                                    if "videoRenderer" in item:
                                        video_renderer = item["videoRenderer"]
                                        if "videoId" in video_renderer:
                                            final_array.append(video_renderer)

                                final_json = json.dumps(final_array, indent=2)
                                return jsonify(final_array)

    return jsonify({'error': 'Data not found'})

if __name__ == '__main__':
    app.run(debug=True)
