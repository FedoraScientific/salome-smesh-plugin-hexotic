# Copyright (C) 2007-2014  CEA/DEN, EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

##
# @package HexoticPLUGINBuilder
# Python API for the MG-Hexa meshing plug-in module.

from salome.smesh.smesh_algorithm import Mesh_Algorithm
from salome.smesh.smeshBuilder import AssureGeomPublished

# import HexoticPlugin module if possible
noHexoticPlugin = 0
try:
    import HexoticPlugin
except ImportError:
    noHexoticPlugin = 1
    pass

#----------------------------
# Mesh algo type identifiers
#----------------------------

## Algorithm type: MG-Hexa hexahedron 3D algorithm, see Hexotic_Algorithm
MG_Hexa = "MG-Hexa"
Hexotic = MG_Hexa

#----------------------------
# Algorithms
#----------------------------

## Defines a hexahedron 3D algorithm
#
#  It is created by calling smeshBuilder.Mesh.Hexahedron( smeshBuilder.MG_Hexa, geom=0 )
class Hexotic_Algorithm(Mesh_Algorithm):

    ## name of the dynamic method in smeshBuilder.Mesh class
    #  @internal
    meshMethod = "Hexahedron"
    ## type of algorithm used with helper function in smeshBuilder.Mesh class
    #  @internal
    algoType   = MG_Hexa
    ## doc string of the method in smeshBuilder.Mesh class
    #  @internal
    docHelper  = "Creates hexahedron 3D algorithm for volumes"

    ## Private constructor.
    #  @param mesh parent mesh object algorithm is assigned to
    #  @param geom geometry (shape/sub-shape) algorithm is assigned to;
    #              if it is @c 0 (default), the algorithm is assigned to the main shape
    def __init__(self, mesh, geom=0):
        Mesh_Algorithm.__init__(self)
        if noHexoticPlugin: print "Warning: HexoticPlugin module unavailable"
        self.Create(mesh, geom, MG_Hexa, "libHexoticEngine.so")
        self.params = None
        pass

    ## Defines "SetMinMaxHexes" hypothesis to give two MG-Hexa parameters
    #  @param min minimal level of recursive partitioning on the initial octree cube
    #  @param max maximal level of recursive partitioning on the initial octree cube
    #  @return hypothesis object
    def SetMinMaxHexes(self, min=3, max=8):
        self.Parameters().SetHexesMinLevel(min)
        self.Parameters().SetHexesMaxLevel(max)
        return self.Parameters()

    ## Defines "SetMinMaxSize" hypothesis to give two MG-Hexa parameters
    #  @param min minimal element's size
    #  @param max maximal element's size
    #  @return hypothesis object
    def SetMinMaxSize(self, min, max):
        self.Parameters().SetMinSize(min)
        self.Parameters().SetMaxSize(max)
        return self.Parameters()
         
    ## Sets a size map
    #  @param theObject geometrical object to assign local size to
    #  @param theSize local size on the given object
    #  @return hypothesis object
    def SetSizeMap(self, theObject, theSize):
        AssureGeomPublished( self.mesh, theObject )
        if theSize <= 0:
          raise ValueError, "The size must be > 0"
        self.Parameters().SetSizeMap(theObject, theSize)
        return self.Parameters()
      
    ## Unsets a size map : this is meant to be used only by the dump
    #  @param theObject geometrical object to unassign local size
    #  @return hypothesis object
    def UnsetSizeMap(self, theObject):
        AssureGeomPublished( self.mesh, theObject )
        self.Parameters().UnsetSizeMap(theObject)
        return self.Parameters()

    ## (OBSOLETE) Defines "MinMaxQuad" hypothesis to give three MG-Hexa parameters
    #  @param min minimal level of recursive partitioning on the initial octree cube
    #  @param max maximal level of recursive partitioning on the initial octree cube
    #  @param quad not documented
    #  @return hypothesis object
    def MinMaxQuad(self, min=3, max=8, quad=True):
        print "WARNING: Function MinMaxQuad is deprecated, use SetMinMaxHexes instead"
        return self.SetMinMaxHexes(min, max)

    ## Defines hypothesis having several parameters
    #  @return hypothesis object
    def Parameters(self):
        if not self.params:
            self.params = self.Hypothesis("MG-Hexa Parameters", [],
                                          "libHexoticEngine.so", UseExisting=0)
            pass
        return self.params


    pass # end of Hexotic_Algorithm class
