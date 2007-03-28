//  HexoticPlugin : C++ implementation
//
//  Copyright (C) 2006  OPEN CASCADE, CEA/DEN, EDF R&D
// 
//  This library is free software; you can redistribute it and/or 
//  modify it under the terms of the GNU Lesser General Public 
//  License as published by the Free Software Foundation; either 
//  version 2.1 of the License. 
// 
//  This library is distributed in the hope that it will be useful, 
//  but WITHOUT ANY WARRANTY; without even the implied warranty of 
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
//  Lesser General Public License for more details. 
// 
//  You should have received a copy of the GNU Lesser General Public 
//  License along with this library; if not, write to the Free Software 
//  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA 
// 
//  See http://www.opencascade.org/SALOME/ or email : webmaster.salome@opencascade.org 
//
//
// File      : HexoticPlugin_Hypothesis.hxx
// Author    : Lioka RAZAFINDRAZAKA (CEA)
// Date      : 2006/06/30
// Project   : SALOME
// $Header: /home/server/cvs/HexoticPLUGIN/HexoticPLUGIN_SRC/src/HexoticPlugin/HexoticPlugin_Hypothesis.hxx,v 1.2 2006/05/06 08:54:13 jfa Exp $
//=============================================================================

#ifndef _HexoticPlugin_Hypothesis_HXX_
#define _HexoticPlugin_Hypothesis_HXX_

#include "SMESH_Hypothesis.hxx"
#include "Utils_SALOME_Exception.hxx"

//  Parameters for work of Hexotic
//

class HexoticPlugin_Hypothesis: public SMESH_Hypothesis
{
public:

  HexoticPlugin_Hypothesis(int hypId, int studyId, SMESH_Gen * gen);

  void SetHexesMinLevel(int theVal);
  int GetHexesMinLevel() const { return _hexesMinLevel; }

  void SetHexesMaxLevel(int theVal);
  int GetHexesMaxLevel() const { return _hexesMaxLevel; }

  void SetHexoticQuadrangles(bool theVal);
  bool GetHexoticQuadrangles() const { return _hexoticQuadrangles; }

  // the parameters default values 

  static int GetDefaultHexesMinLevel();
  static int GetDefaultHexesMaxLevel();
  static bool GetDefaultHexoticQuadrangles();

  // Persistence
  virtual ostream & SaveTo(ostream & save);
  virtual istream & LoadFrom(istream & load);
  friend ostream & operator <<(ostream & save, HexoticPlugin_Hypothesis & hyp);
  friend istream & operator >>(istream & load, HexoticPlugin_Hypothesis & hyp);

  /*!
   * \brief Does nothing
   * \param theMesh - the built mesh
   * \param theShape - the geometry of interest
   * \retval bool - always false
   */
  virtual bool SetParametersByMesh(const SMESH_Mesh* theMesh, const TopoDS_Shape& theShape);

private:
  int   _hexesMinLevel;
  int   _hexesMaxLevel;
  bool  _hexoticQuadrangles;
};

#endif
