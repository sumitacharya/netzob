# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+ 
#| Standard library imports
#+---------------------------------------------------------------------------+
import logging

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+
from netzob.Common.Models.AbstractMessage import AbstractMessage
from netzob.Common.Models.Factories.FileMessageFactory import FileMessageFactory


#+---------------------------------------------------------------------------+
#| FileMessage :
#|     Definition of a file message
#+---------------------------------------------------------------------------+
class FileMessage(AbstractMessage):
    def __init__(self, id, timestamp, data, filename, creationDate, modificationDate, owner, size, lineNumber):
        AbstractMessage.__init__(self, id, timestamp, data, "File")
        self.filename = filename
        self.creationDate = creationDate
        self.modificationDate = modificationDate
        self.owner = owner
        self.size = size
        self.lineNumber = lineNumber
        
        # create logger with the given configuration
        self.log = logging.getLogger('netzob.Common.Models.FileMessage.py')
    
    #+-----------------------------------------------------------------------+
    #| getFactory
    #| @return the associated factory
    #+-----------------------------------------------------------------------+
    def getFactory(self):
        return FileMessageFactory
    
    #+-----------------------------------------------------------------------+
    #| getProperties
    #|     Computes and returns the properties of the current message
    #| @return an array with all the properties [[key,val],...]
    #+-----------------------------------------------------------------------+
    def getProperties(self):
        properties = []        
        properties.append(['ID', str(self.getID())])
        properties.append(['Type', self.getType()])
        properties.append(['Timestamp', self.getTimestamp()])
        properties.append(['Filename', self.getFilename()])
        properties.append(['Creation Date', self.getCreationDate()])
        properties.append(['Modification Date', self.getModificationDate()])
        properties.append(['Owner', self.getOwner()])
        properties.append(['Size', self.getSize()])
        properties.append(['Line number', self.getLineNumber()])        
        properties.append(['Data', self.getStringData()])
        
        return properties 
        
    #+---------------------------------------------- 
    #| GETTERS : 
    #+----------------------------------------------
    def getLineNumber(self):
        return self.lineNumber
    def getFilename(self):
        return self.filename
    def getCreationDate(self):
        return self.creationDate
    def getModificationDate(self):
        return self.modificationDate
    def getOwner(self):
        return self.owner
    def getSize(self):
        return self.size
       
    #+---------------------------------------------- 
    #| SETTERS : 
    #+----------------------------------------------
    def setLineNumber(self, lineNumber):
        try :
            self.lineNumber = int(lineNumber)
        except :
            self.log.warning("Impossible to set the given line number since its not an int !")
    def setFilename(self, filename):
        self.filename = filename
    def setCreationDate(self, creationDate):
        self.creationDate = creationDate
    def setModificationDate(self, modificationDate):
        self.modificationDate = modificationDate
    def setOwner(self, owner):
        self.owner = owner
    def setSize(self, size):
        self.size = size
  

