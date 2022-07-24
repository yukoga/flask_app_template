# -*- coding: utf-8 -*-

# Copyright 2022 yukoga. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from datetime import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
from flaskapp.db import get_db


bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/', methods=('GET', 'POST'))
def index():
    posts = []
    posts.append({
        'id': 1,
        'title': 'First content',
        'body': 'This is the first content of flask app.',
        'created': datetime.strptime('2022-07-24 01:11:01', '%Y-%m-%d %H:%M:%S'),
        'username': 'user no.1'
    })
    posts.append({
        'id': 2,
        'title': 'Second content',
        'body': 'This is the second content of flask app.',
        'created': datetime.strptime('2022-07-25 12:53:11', '%Y-%m-%d %H:%M:%S'),
        'username': 'user no.2'
    })

    return render_template('posts/index.html', posts=posts)
