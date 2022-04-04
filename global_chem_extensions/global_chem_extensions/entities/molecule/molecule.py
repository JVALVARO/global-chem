#!/usr/bin/env python3
#
# GlobalChemExtensions - GlobalChem Molecule

# -------------------------------------------

# Imports
# -------

from rdkit import Chem
import rdkit.Chem.Descriptors as Descriptors

# Conversion SMILES Imports
# -------------------------

import deepsmiles
import selfies as sf
import partialsmiles as ps

from rdkit import Chem
from pysmiles import read_smiles
from molvs import validate_smiles


# Local Imports
# -------------

from global_chem import GlobalChem

class GlobalChemMolecule(object):


    __version__ = '0.0.1'

    def __init__(
            self,
            smiles,
            name = None,
            cgenff_stream_file = None,
            gaff_frcmod_file = None,
            cgenff_molecule = None,
            gaff2_molecule = None
    ):

        '''

        Arguments:
            smiles (String): Chem.MolFromSmiles(i)
            cgenff_stream_file (String): Whether the user would like it with a cgenff entity attached
            gaff_frcmod_file (String): Whether the user would like it with a gaff2 entity attached
            cgenff_molecule (CGenFFMolecule Object): Quick hack to pass it and not deal with file path issues
            gaff2_molecule (GaFF2Molecule Object): Quick hack to pass the Gaff2 Molecule and not deal with file path issues

        '''

        self.name = name
        self.smiles = smiles
        self.molecule = Chem.MolFromSmiles(self.smiles)

        if cgenff_stream_file:
            self._read_cgenff_molecule(cgenff_stream_file, cgenff_molecule)

        if gaff_frcmod_file:
            self._read_gaff2_molecule(gaff_frcmod_file, gaff2_molecule)

        self.attributes = {}
        self.attributes['name'] = self.name
        self.attributes['smiles'] = self.smiles

        self._determine_attributes()

        self.converter = deepsmiles.Converter(rings=True, branches=True)


    def get_attributes(self):

        '''

        Returns the attributes

        '''

        return self.attributes

    def get_rdkit_molecule(self):

        '''

        Returns the RDKit Molecule

        '''

        return Chem.MolFromSmiles(self.smiles)

    def get_cgenff_molecule(self):

        '''

        Returns:
            cgenff_molecule (GlobalChem Object): the molecule object
        '''

        return self.cgenff_molecule

    def _read_cgenff_molecule(self, cgenff_stream_file, cgenff_molecule):

        '''

        Initialize the CGenFF Molecule

        Arguments:
            cgenff_stream_file (String): Stream file of CGenFF
            cgenff_molecule (GlobalChem Object): CGenFFMolecule Object

        '''

        self.cgenff_molecule = cgenff_molecule(stream_file = cgenff_stream_file)

    def get_gaff2_molecule(self):

        '''

        Returns:
            gaff2_molecule (GlobalChem Object): the molecule object
        '''

        return self.gaff2_molecule

    def _read_gaff2_molecule(self, gaff2_frcmod_file, gaff2_molecule):

        '''

        Initialize the CGenFF Molecule

        Arguments:
            gaff2_frcmod_file (String): FRCMOD file of GAFF2
            gaff2_molecule (GlobalChem Object): GAFF2Molecule Object

        '''

        self.gaff2_molecule = gaff2_molecule(frcmod_file = gaff2_frcmod_file)

    def _determine_attributes(self):

        '''

        Fetch the Attributes of the molecule

        '''


        molecular_weight = Descriptors.ExactMolWt(self.molecule)
        logp = Descriptors.MolLogP(self.molecule)
        h_bond_donor = Descriptors.NumHDonors(self.molecule)
        h_bond_acceptors = Descriptors.NumHAcceptors(self.molecule)
        rotatable_bonds = Descriptors.NumRotatableBonds(self.molecule)
        number_of_atoms = Chem.rdchem.Mol.GetNumAtoms(self.molecule)
        molar_refractivity = Chem.Crippen.MolMR(self.molecule)
        topological_surface_area_mapping = Chem.QED.properties(self.molecule).PSA
        formal_charge = Chem.rdmolops.GetFormalCharge(self.molecule)
        heavy_atoms = Chem.rdchem.Mol.GetNumHeavyAtoms(self.molecule)
        num_of_rings = Chem.rdMolDescriptors.CalcNumRings(self.molecule)


        self.attributes['molecular_weight'] = molecular_weight
        self.attributes['logp'] = logp
        self.attributes['h_bond_donor'] = h_bond_donor
        self.attributes['h_bond_acceptors'] = h_bond_acceptors
        self.attributes['rotatable_bonds'] = rotatable_bonds
        self.attributes['number_of_atoms'] = number_of_atoms
        self.attributes['molar_refractivity'] = molar_refractivity
        self.attributes['topological_surface_area_mapping'] = topological_surface_area_mapping
        self.attributes['formal_charge'] = formal_charge
        self.attributes['heavy_atoms'] = heavy_atoms
        self.attributes['num_of_rings'] = num_of_rings

    def determine_name(self):

        '''

        Determine the Name of a molecule if available

        '''


        gc = GlobalChem()
        smiles_list = gc.get_all_smiles()
        name_list = gc.get_all_names()

        name_found = False

        for i, smiles in enumerate(smiles_list):

            name = name_list[i]

            if smiles == self.smiles and not name_found:
                self.name = name
                self.attributes['name'] = name
                name_found = True

    def get_partial_smiles(self, partial=None):

        '''

        Get's the partial SMILES mol object

        Arguments:
            partial (Bool): whether the user is passing in partial SMILES
        '''

        return ps.ParseSmiles(self.smiles, partial=partial)

    def get_pysmiles(self):

        '''

        Gets the PySMILES mol object

        '''

        return read_smiles(self.smiles)

    def encode_deep_smiles(self):

        '''

        Gets the DeepSMILES mol Object

        '''

        return self.converter.encode(self.smiles)

    def decode_deep_smiles(self):

        '''

        Decodes the DeepSMILES molObject

        '''

        return self.converter.decode(self.smiles)

    def encode_selfies(self):

        '''

        Encodes into the Selfies Object

        '''

        return sf.encoder(self.smiles)

    def decode_selfies(self):

        '''

        Decodes the Selfies Object

        '''

        return sf.decoder(self.smiles)

    def validate_molvs(self):

        '''

        Validate the SMILES with MOLVS

        '''

        return validate_smiles(self.smiles)


