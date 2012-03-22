#!/usr/bin/python2.6.5
# -*- coding: utf-8 -*-
#
# Copyright 2011 Christos Spiliopoulos.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



__authors__ = [
  '"Christos Spiliopoulos" <santos.koniordos@gmail.com>',
]



class IndexBase(object):
    '''
    A base class representing a "connection" with a redis server ( db )
    
    Attributes:
    
       _cardinality_key : a special key of _dict_key denoting the total number of documents in our corpus
       _set_key : a special key holding our unique docIDs currently present in the corpus
       db : the name of redis database (server)
       pipe : redis pipeline object
       

    NOTE: this class (and its descendants) is not thread-safe, thus create a new object every time you need its functionality, per process/thread.
          DO NOT EVER SHARE SUCH AN OBJECT !!!
    

    '''
    
    def __init__(self, **kwargs):
        self._cardinality_key = kwargs.get('cardinality_key',"$CARDINALITY$") 
        self._set_key = kwargs.get('set_key',"$DOCIDS$")
        self.db = kwargs.get('db',"") 
        self.pipe = self.db.pipeline()
        
    def flush(self):
        ''' executes the pipeline, returns a list of results '''
        return self.pipe.execute()
    
    def drop(self):
        ''' drops the entire index '''
        return self.db.flushdb()   



