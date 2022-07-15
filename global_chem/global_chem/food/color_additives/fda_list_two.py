#!/usr/bin/env python3
#
# GlobalChem - FDA List Two
#
# -------------------------

class FDAListTwo(object):

    def __init__(self):

        self.name = 'fda_list_two'

    @staticmethod
    def get_smiles():

        smiles = {
            'd&c black #2': '[C]',
            'd&c black #3': '[O-]P(=O)([O-])[O-].[Ca+2].[Ca+2].[Ca+2].C(=O)([O-])[O-].[Ca+2].[C]',
            'd&c green #5': 'CC1=CC(=C(C=C1)NC2=C3C(=C(C=C2)NC4=C(C=C(C=C4)C)S(=O)(=O)[O-])C(=O)C5=CC=CC=C5C3=O)S(=O)(=O)[O-].[Na+].[Na+]',
            'd&c orange #5': 'C1=CC=C2C(=C1)C(=O)OC23C4=CC(=C(C(=C4OC5=C(C(=C(C=C35)Br)O)Br)Br)O)Br.C1=CC=C2C(=C1)C(=O)OC23C4=C(C(=C(C=C4)O)Br)OC5=C3C=CC(=C5Br)O.C1=CC=C(C(=C1)C2=C3C=C(C(=O)C(=C3OC4=C(C(=C(C=C24)Br)[O-])Br)Br)Br)C(=O)[O-].[Na+].[Na+]',
            'd&c red #6': 'CC1=CC(=C(C=C1)N=NC2=C(C(=CC3=CC=CC=C32)C(=O)O)[O-])S(=O)(=O)[O-].[Na+].[Na+]',
            'd&c red #7': 'CC1=CC(=C(C=C1)N=NC2=C(C(=CC3=CC=CC=C32)C(=O)O)[O-])S(=O)(=O)[O-].[Ca+2]',
            'd&c red #21': 'C1=CC=C2C(=C1)C(=O)OC23C4=CC(=C(C(=C4OC5=C(C(=C(C=C35)Br)O)Br)Br)O)Br',
            'd&c red #22': 'C1=CC=C(C(=C1)C2=C3C=C(C(=O)C(=C3OC4=C(C(=C(C=C24)Br)[O-])Br)Br)Br)C(=O)[O-].[Na+].[Na+]',
            'd&c red #27': 'C1=C2C(=C(C(=C1Br)O)Br)OC3=C(C(=C(C=C3C24C5=C(C(=C(C(=C5Cl)Cl)Cl)Cl)C(=O)O4)Br)O)Br',
            'd&c red #28': 'C1=C2C(=C3C=C(C(=O)C(=C3OC2=C(C(=C1Br)[O-])Br)Br)Br)C4=C(C(=C(C(=C4Cl)Cl)Cl)Cl)C(=O)[O-].[Na+].[Na+]',
            'd&c red #30': 'CC1=CC(=CC2=C1C(=O)C(=C3C(=O)C4=C(S3)C=C(C=C4C)Cl)S2)Cl',
            'd&c red #33': 'C1=CC=C(C=C1)N=NC2=C(C3=C(C=C(C=C3C=C2S(=O)(=O)O)S(=O)(=O)O)N)O',
            'd&c red #36': 'C1=CC=C2C(=C1)C=CC(=C2N=NC3=C(C=C(C=C3)[N+](=O)[O-])Cl)O',
            'd&c yellow #10': 'C1=CC=C2C(=C1)C(=O)C(C2=O)C3=NC4=C(C=C(C=C4C=C3)S(=O)(=O)O)S(=O)(=O)O',
            'd&c lakes': '[Na+].[Zr+2].[Ca+2]',
        }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {
            'd&c black #2': '[#6]',
            'd&c black #3': '[#8-]-[#15](=[#8])(-[#8-])-[#8-].[Ca+2].[Ca+2].[Ca+2].[#6](=[#8])(-[#8-])-[#8-].[Ca+2].[#6]',
            'd&c green #5': '[#6]-[#6]1:[#6]:[#6](:[#6](:[#6]:[#6]:1)-[#7]-[#6]1:[#6]2:[#6](:[#6](:[#6]:[#6]:1)-[#7]-[#6]1:[#6](:[#6]:[#6](:[#6]:[#6]:1)-[#6])-[#16](=[#8])(=[#8])-[#8-])-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-2=[#8])-[#16](=[#8])(=[#8])-[#8-].[Na+].[Na+]',
            'd&c orange #5': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1)-[#6](=[#8])-[#8]-[#6]-21-[#6]2:[#6]:[#6](:[#6](:[#6](:[#6]:2-[#8]-[#6]2:[#6](:[#6](:[#6](:[#6]:[#6]:2-1)-[#35])-[#8])-[#35])-[#35])-[#8])-[#35].[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1)-[#6](=[#8])-[#8]-[#6]-21-[#6]2:[#6](:[#6](:[#6](:[#6]:[#6]:2)-[#8])-[#35])-[#8]-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2-[#35])-[#8].[#6]1:[#6]:[#6]:[#6](:[#6](:[#6]:1)-[#6]1:[#6]2:[#6]:[#6](:[#6](=[#8]):[#6](:[#6]-2:[#8]:[#6]2:[#6](:[#6](:[#6](:[#6]:[#6]:1:2)-[#35])-[#8-])-[#35])-[#35])-[#35])-[#6](=[#8])-[#8-].[Na+].[Na+]',
            'd&c red #6': '[#6]-[#6]1:[#6]:[#6](:[#6](:[#6]:[#6]:1)-[#7]=[#7]-[#6]1:[#6](:[#6](:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2)-[#6](=[#8])-[#8])-[#8-])-[#16](=[#8])(=[#8])-[#8-].[Na+].[Na+]',
            'd&c red #7': '[#6]-[#6]1:[#6]:[#6](:[#6](:[#6]:[#6]:1)-[#7]=[#7]-[#6]1:[#6](:[#6](:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2)-[#6](=[#8])-[#8])-[#8-])-[#16](=[#8])(=[#8])-[#8-].[Ca+2]',
            'd&c red #21': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1)-[#6](=[#8])-[#8]-[#6]-21-[#6]2:[#6]:[#6](:[#6](:[#6](:[#6]:2-[#8]-[#6]2:[#6](:[#6](:[#6](:[#6]:[#6]:2-1)-[#35])-[#8])-[#35])-[#35])-[#8])-[#35]',
            'd&c red #22': '[#6]1:[#6]:[#6]:[#6](:[#6](:[#6]:1)-[#6]1:[#6]2:[#6]:[#6](:[#6](=[#8]):[#6](:[#6]-2:[#8]:[#6]2:[#6](:[#6](:[#6](:[#6]:[#6]:1:2)-[#35])-[#8-])-[#35])-[#35])-[#35])-[#6](=[#8])-[#8-].[Na+].[Na+]',
            'd&c red #27': '[#6]1:[#6]2:[#6](:[#6](:[#6](:[#6]:1-[#35])-[#8])-[#35])-[#8]-[#6]1:[#6](:[#6](:[#6](:[#6]:[#6]:1-[#6]-21-[#6]2:[#6](:[#6](:[#6](:[#6](:[#6]:2-[#17])-[#17])-[#17])-[#17])-[#6](=[#8])-[#8]-1)-[#35])-[#8])-[#35]',
            'd&c red #28': '[#6]1:[#6]2:[#6](:[#6]3:[#6]:[#6](:[#6](=[#8]):[#6](:[#6]-3:[#8]:[#6]:2:[#6](:[#6](:[#6]:1-[#35])-[#8-])-[#35])-[#35])-[#35])-[#6]1:[#6](:[#6](:[#6](:[#6](:[#6]:1-[#17])-[#17])-[#17])-[#17])-[#6](=[#8])-[#8-].[Na+].[Na+]',
            'd&c red #30': '[#6]-[#6]1:[#6]:[#6](:[#6]:[#6]2:[#6]:1-[#6](=[#8])-[#6](=[#6]1-[#6](=[#8])-[#6]3:[#6](-[#16]-1):[#6]:[#6](:[#6]:[#6]:3-[#6])-[#17])-[#16]-2)-[#17]',
            'd&c red #33': '[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]=[#7]-[#6]1:[#6](:[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2:[#6]:[#6]:1-[#16](=[#8])(=[#8])-[#8])-[#16](=[#8])(=[#8])-[#8])-[#7])-[#8]',
            'd&c red #36': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1):[#6]:[#6]:[#6](:[#6]:2-[#7]=[#7]-[#6]1:[#6](:[#6]:[#6](:[#6]:[#6]:1)-[#7+](=[#8])-[#8-])-[#17])-[#8]',
            'd&c yellow #10': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1)-[#6](=[#8])-[#6](-[#6]-2=[#8])-[#6]1:[#7]:[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2:[#6]:[#6]:1)-[#16](=[#8])(=[#8])-[#8])-[#16](=[#8])(=[#8])-[#8]',
            'd&c lakes': '[Na+].[Zr+2].[Ca+2]',
        }

        return smarts

    @staticmethod
    def get_bit_vector():

        bit_vector = {
            'd&c black #2': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'd&c black #3': '00000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000001000000010000000001100000000000000000000000000000000000000000000000000000000000000000000000000000000100000000001000000000000000000000000000000000000000000000000000000000000000000000000000000010000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000',
            'd&c green #5': '01000000000000000000000000000000010100000000000000000000000000001000000000000000000000000000000001000000000000000000000000000000100000000010100000000000000000000000000000001001000000000010010000000000100100000001001000000000000000000001000000000000000000100000000000000000000000000000010100000000000000000000000000110000100000000000000001000000000000101010100000010000000000000000000000000000100000000000000000000000000000000000000000000000000000000000100000000100000000001000000000000000000100000000110000000000',
            'd&c orange #5': '01000000000001000000000000000000100010000000101000000000000000001010100110001000000010000000000100000000000000100000000000000000000001000010000010000000000000000000010010000001000000000000010010010010101100001001001010000000000000000001000100000000100000000010000000000011001000000000000000000001001000000000000000101000011001000000010001000000000000001000100000010000000100000000010010000000000000000000000000000000000100011000000011101000000011000001000100001000001000001001000000000000000010000000000100000000',
            'd&c red #6': '00000000000000000010000100000000010001000000000000000000000000011000000000000000000000000000000000000000001001000000000000000010010000000010100000000000000000000000000000001001000000000010010000000000000100000000011000000000000000000001000100000000000000000000010000000001000000000000010100010001000000000000100000010001000010000000011001000000000000100000100000010000000000000000010000000100100000000000000000000000000100000000000000000000000000000000110110000000000000110000000000000000000000000000010000000000',
            'd&c red #7': '00000000000000000010000100000000010001000000000000000000000000011000000000000000000000000000000000000000001001000000000000000010010000000010100000000000000000000000000000001001000000000010000000000000000100000000011000000000000000000001000100000000000000000000010000000001000000000000110100010001000000000000100000010001000010000000011001000000000000100000100000010000000000000000010000000100100000000000000000000000000100000000000000000000000000000000110110000000000000110000000000000000000000000000010000000000',
            'd&c red #21': '00000000000000000000000000000000000010000000000000000000000000001010000000001000000000000000000100000000000000000000000000000000000000000010000010000000000000000000010010000001000000000000000000000000001000000000001010000000000000000001000000000000000000000010000000000010001000000000000000000001001000000000000000100000011001000000000001000000000000001000100000010000000100000000000010000000000000000000000000000000000000001000000000101000000010000000000000001000001000001001000000000000000000000000000000000000',
            'd&c red #22': '01000000000001000000000000000000100000000000101000000000000000001000100010000000000000000000000100000000000000100000000000000000000001000010000010000000000000000000000000000001000000000000010000010010101100001001001010000000000000000000000100000000000000000000000000000001000000000000000000000001000000000000000000101000010000000000010001000000000000001000100000010000000000000000010000000000000000000000000000000000000100010000000011100000000001000000000100000000000000001000000000000000000010000000000100000000',
            'd&c red #27': '00010000000000010000000000000000000010000000000001000000000000101010000000001000000000000000000100000000000000000000000000000000000000000010000010010000000000000000010010000000000000000000000000000000001000000001000010000000000000000001000000000000000000000010000000000010001000000000000000000001000000000000000000100000011001000000000001000001000000100000100000010000000100000000000010000000000000000000000000000000000000000000000000100000000010000100000000001000000000000001000000000000000000000001000010000000',
            'd&c red #28': '01000000000001000000000000000000100000000000101001000000000000100000100010100000000000000000000100000000000000100000000000000000001001000010000010010000000000000000000000000000000000000000010000010000101100001001000010000000000000100000000100000000000000000000000000000001000000000000000000000001000000000000000000101000010000000000010001000000100000101000100000010000000000000000010000000000000000000000000000000000000000000000000001100000000000000000000100000000000000000000100000000000000010000001001100000000',
            'd&c red #30': '00000000000000000000000000000000010000000000000001000000000000000000000000000000000000000001000000000000000000000000000000000000000000000010000000010000000000000001000000000000000000001010000000000000000000000001000010000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000100000000000000000000101000000000001000000100000010001000000000000000000000000000000000000000000000100000000000000000000010100000000000000100000000000000000000000000000000100000000000000000000011000',
            'd&c red #33': '10000000000001000000000000000000000000000000000100000000000000101010000000000000100000000000000000000000001000000010000000000000010000000010000010010000000000000000001000000001000000000000000010000000001000000000011000000000000000000000000000000000000000000000000000000000001000000000000000000001000000000000000100001011000010000000000001000000000000100000100000010000001000000000000000000100100000100000000000000000000100000000000001000000000001001000100010000000000000000000000000000000000000000000000000000000',
            'd&c red #36': '00000000000000000010000000000000000001000000000001000000000000011010000100000000100000000000000000000000001000000000000000000010010000000010000000010000000000000000000000010001000000100000000000000000000100000000011000000000000000000000000001000000001000000000000000000000010000100000000000000001000000000000100000000001000001100000010001000000000000000000100000010010000000000000000000000000000000000000100000000000000100000001000010000000000000000001000000000000000000010000000100000000000001000000000000000000',
            'd&c yellow #10': '00000000000000000000000000000000000000000000000000000000000000001000000000000000100000000000000000000000000000000010000000000000000000100010000000010000000000000000000000000001000000000000100010000000000100000000101000000000000000000000000000000000000000000000000000000000001010000000000000000001000100000000000000100101000010000000000001000000000000101000100001010000000000000010000001000000100000000000000000000000000000000001000000000000000000000000100010000000000010001001001000000000000000000000000000010000',
            'd&c lakes': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
        }

        return bit_vector