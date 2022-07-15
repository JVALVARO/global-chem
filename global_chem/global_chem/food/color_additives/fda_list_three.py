#!/usr/bin/env python3
#
# GlobalChem - FDA List Three
#
# ---------------------------

class FDAListThree(object):

    def __init__(self):

        self.name = 'fda_list_three'

    @staticmethod
    def get_smiles():

        smiles = {
            'd&C brown #1': 'CC1=CC(=C(C=C1)NN=C2C(=O)C=CC(=NNC3=CC=C(C=C3)S(=O)(=O)[O-])C2=O)C.[Na+]',
            'fD&C red #4': 'CC1=CC(=C(C=C1N=NC2=C(C3=CC=CC=C3C(=C2)S(=O)(=O)O)O)S(=O)(=O)O)C',
            'd&c red #17': 'C1=CC=C(C=C1)N=NC2=CC=C(C=C2)N=NC3=C(C=CC4=CC=CC=C43)O',
            'd&c red #31': 'C1=CC=C(C=C1)N=NC2=C(C(=CC3=CC=CC=C32)C(=O)O)[O-].C1=CC=C(C=C1)N=NC2=C(C(=CC3=CC=CC=C32)C(=O)O)[O-].[Ca+2]',
            'd&c red #34': 'C1=CC=C2C(=C1)C=CC(=C2S(=O)(=O)[O-])N=NC3=C(C(=CC4=CC=CC=C43)C(=O)O)[O-].[Ca+2]',
            'd&c red #39': 'C1=CC=C(C(=C1)C(=O)O)N=NC2=CC=C(C=C2)N(CCO)CCO',
            'd&c violet #2': 'CC1=CC=C(C=C1)NC2=C3C(=C(C=C2)O)C(=O)C4=CC=CC=C4C3=O',
            'd&c blue #4': 'CCN(CC1=CC=C(C=C1)S(=O)(=O)[O-])C2=CC=C(C=C2)C(=C3C=CC(=[N+](CC)CC4=CC=C(C=C4)S(=O)(=O)[O-])C=C3)C5=CC=CC=C5S(=O)(=O)[O-].[NH4+].[NH4+]',
            'd&c green #6': 'CC1=CC=C(C=C1)NC2=C3C(=C(C=C2)NC4=CC=C(C=C4)C)C(=O)C5=CC=CC=C5C3=O',
            'd&c green #8': 'C1=CC2=C3C(=C(C=C2S(=O)(=O)[O-])S(=O)(=O)[O-])C=CC4=C(C=C(C1=C43)O)S(=O)(=O)[O-].[Na+].[Na+].[Na+]',
            'd&c yellow #7': 'C1=CC2=C(C=C1S(=O)(=O)[O-])C(=C(C=C2[N+](=O)[O-])[N+](=O)[O-])[O-].[Na+].[Na+]',
            'd&c yellow #8': 'C1=CC=C(C(=C1)C2=C3C=CC(=O)C=C3OC4=C2C=CC(=C4)[O-])C(=O)[O-].[Na+].[Na+]',
            'd&c yellow #11': 'C1=CC=C2C(=C1)C=CC(=N2)C3C(=O)C4=CC=CC=C4C3=O',
            'd&c orange #4': 'C1=CC=C2C(=C1)C=CC(=C2N=NC3=CC=C(C=C3)S(=O)(=O)O)O.[Na+]',
            'd&c orange #10': 'C1=CC2=C(C(=C1)I)C(=O)OC23C4=C(C=C(C=C4)O)OC5=C3C=CC(=C5I)O',
            'd&c orange #11': 'C1=CC=C2C(=C1)C(=O)OC23C4=C(C=C(C=C4)O)OC5=C3C=CC(=C5)O',
        }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {
            'd&c brown #1': '[#6]-[#6]1:[#6]:[#6](:[#6](:[#6]:[#6]:1)-[#7]-[#7]=[#6]1:[#6](=[#8]):[#6]:[#6]:[#6](=[#7]-[#7]-[#6]2:[#6]:[#6]:[#6](:[#6]:[#6]:2)-[#16](=[#8])(=[#8])-[#8-]):[#6]:1=[#8])-[#6].[Na+]',
            'fd&c red #4': '[#6]-[#6]1:[#6]:[#6](:[#6](:[#6]:[#6]:1-[#7]=[#7]-[#6]1:[#6](:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2:[#6](:[#6]:1)-[#16](=[#8])(=[#8])-[#8])-[#8])-[#16](=[#8])(=[#8])-[#8])-[#6]',
            'd&c red #17': '[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]=[#7]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]=[#7]-[#6]1:[#6](:[#6]:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2)-[#8]',
            'd&c red #31': '[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]=[#7]-[#6]1:[#6](:[#6](:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2)-[#6](=[#8])-[#8])-[#8-].[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]=[#7]-[#6]1:[#6](:[#6](:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2)-[#6](=[#8])-[#8])-[#8-].[Ca+2]',
            'd&c red #34': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1):[#6]:[#6]:[#6](:[#6]:2-[#16](=[#8])(=[#8])-[#8-])-[#7]=[#7]-[#6]1:[#6](:[#6](:[#6]:[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:1:2)-[#6](=[#8])-[#8])-[#8-].[Ca+2]',
            'd&c red #39': '[#6]1:[#6]:[#6]:[#6](:[#6](:[#6]:1)-[#6](=[#8])-[#8])-[#7]=[#7]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7](-[#6]-[#6]-[#8])-[#6]-[#6]-[#8]',
            'd&c violet #2': '[#6]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]-[#6]1:[#6]2:[#6](:[#6](:[#6]:[#6]:1)-[#8])-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-2=[#8]',
            'd&c blue #4': '[#6]-[#6]-[#7](-[#6]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#16](=[#8])(=[#8])-[#8-])-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6](=[#6]1-[#6]=[#6]-[#6](=[#7+](-[#6]-[#6])-[#6]-[#6]2:[#6]:[#6]:[#6](:[#6]:[#6]:2)-[#16](=[#8])(=[#8])-[#8-])-[#6]=[#6]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#16](=[#8])(=[#8])-[#8-].[#7H4+].[#7H4+]',
            'd&c green #6': '[#6]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]-[#6]1:[#6]2:[#6](:[#6](:[#6]:[#6]:1)-[#7]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6])-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-2=[#8]',
            'd&c green #8': '[#6]1:[#6]:[#6]2:[#6]3:[#6](:[#6](:[#6]:[#6]:2-[#16](=[#8])(=[#8])-[#8-])-[#16](=[#8])(=[#8])-[#8-]):[#6]:[#6]:[#6]2:[#6](:[#6]:[#6](:[#6]:1:[#6]:3:2)-[#8])-[#16](=[#8])(=[#8])-[#8-].[Na+].[Na+].[Na+]',
            'd&c yellow #7': '[#6]1:[#6]:[#6]2:[#6](:[#6]:[#6]:1-[#16](=[#8])(=[#8])-[#8-]):[#6](:[#6](:[#6]:[#6]:2-[#7+](=[#8])-[#8-])-[#7+](=[#8])-[#8-])-[#8-].[Na+].[Na+]',
            'd&c yellow #8': '[#6]1:[#6]:[#6]:[#6](:[#6](:[#6]:1)-[#6]1:[#6]2:[#6]:[#6]:[#6](=[#8]):[#6]:[#6]-2:[#8]:[#6]2:[#6]:1:[#6]:[#6]:[#6](:[#6]:2)-[#8-])-[#6](=[#8])-[#8-].[Na+].[Na+]',
            'd&c yellow #11': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1):[#6]:[#6]:[#6](:[#7]:2)-[#6]1-[#6](=[#8])-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2-[#6]-1=[#8]',
            'd&c orange #4': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1):[#6]:[#6]:[#6](:[#6]:2-[#7]=[#7]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#16](=[#8])(=[#8])-[#8])-[#8].[Na+]',
            'd&c orange #10': '[#6]1:[#6]:[#6]2:[#6](:[#6](:[#6]:1)-[#53])-[#6](=[#8])-[#8]-[#6]-21-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#8])-[#8]-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2-[#53])-[#8]',
            'd&c orange #11': '[#6]1:[#6]:[#6]:[#6]2:[#6](:[#6]:1)-[#6](=[#8])-[#8]-[#6]-21-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#8])-[#8]-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#8]',
        }

        return smarts

    @staticmethod
    def get_bit_vector():

        bit_vector = {
            'd&C brown #1': '00000000000001000000000000000000010000000000100000000000000000000000000000000000000000000000000000000000000000001000000000000000100000000010000000000000000000000000000000000000000000000010010100100100101110000000011000000000000000000001000000010000000000010000000000000000000000000000010100000000000000010000000100110001100000000001000101001000100000100000100100010001010000000000000000000000000000000000000010000000001000000000010000000000000000000000100000000000000000000000100000001000000000000000010000000000',
            'fD&C red #4': '00000000010000000010000000000000011001000000000000000000000000001010000000000000100000000000000000000100000000000010000000000000000000000010000000000000000010000000000010000001000000000010000000000000001000000000011000000000001000000000000000000000100000100000000000000000000000000000000000000001000000000000000000000000000010000000010001000000000010100000100000010001000000000000000000000000100000000000000000000000000100000000000000000000000000000000100000000000010000010001000000000000000000000000000000000000',
            'd&c red #17': '00000000000000000000000000000000000001000000000100000000000000111010000100000000100000000000000000000000001000000000000000000000010000000000000010000000000000000000000000000001000000000000000000000000001100000000011000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000100000000011000001000000010001000000000000000000100000000000000000000000000000000100000000000000000000000000000100000000000000000000000000000001000000000000000000000000000100000000000000000000000000000000',
            'd&c red #31': '00000000000000000000000100000000000001000000000100000000000000111000000000000000000000000000000000000000001001000000000000000000010000000010000010000000000000000000000000000001000000000000000000000000000100000000011000000000000000000000000100000000000000000000010000000001000000000000100000000001000000000000100000000011000010000000011001000000000000000000100000010000000000000000010000000100000000000000000000000000000100000000000000000000000000000000010110000000000000000000000000000000000000000000000000000000',
            'd&c red #34': '00000000000000000010000100000000000001000000000000000000000100011000000000000000100000000000000000000000001001000000000000000010010000000010000000000000000000000000000000000001000000000000000000000000000100000000011000000000000000000000000100000000100000000000010000000001000000000000110000000001000000000010100000010001000010000000011001000000000000100000100000010000000000000000010000000100000000000000000000000000000100000000000001000000000000000000110110000000000000010000000000000000000000000000000000000100',
            'd&c red #39': '00000000000000000010000100001000000000000000000110000100000000001000000010000000100000000010000000000000000000000000000000000000000000000010000010000001000000000000000000000001000000000000000000000000001000000000011000000010000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000110000000000000000001000000000000000010100000000000010000000000010000000100010000000000000000000001000100010000000000000000000000001000000110000000000000010100000000000000000000000000000000000000',
            'd&c violet #2': '01000000000000000000000000000000010000000000000000000000000000001010000100000000000000000000000000000000000000000000000000000000100000000010000000000000000000000000000000000001000000000010000100000000100000000001001000000000000000000001000000000000000000100000000000000000000000000000000100000001000000000001000000100000100000000001000001000000000000001010100000000000000000000000000010000000000000000000000000100000000000000000000000000000000000010001100000000100000000001000000000000000000100000000100000000000',
            'd&c blue #4': '00000000010000000000000000000000010100000000000100000100000000001000000010000000100000000000000000000000000000000010000000110000000000000010101101000001000000000100000000010011000010000000000000000000000100000000001010100000000100000000001000000000010110000000000000000000000000001000010000000011000000000000001100010001000000000000000001000000000000100000100001000001010000000000000000000001100000000000000000000000000010010001010000000000000000001000100100000000000000000000000011000000000000000000000010010000',
            'd&c green #6': '01000000000000000000000000000000010000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000100000000010000000000000000000000000000000000001000000000010000100000000100000000001001000000000000000000001000000000000000000100000000000000000000000000000000100000000000000000001000000100000100000000001000001000000000000001010100000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000100000000100000000001000000000000000000100000000100000000000',
            'd&c green #8': '00000000000000000000000000000000000000000000000000000000000000000010000100000000000000000000000000000000000000000000000000000000000000000010100001000000000000000000100000000000000100000000010000000101000100000000001000000000000000000000000000000000000000000000000000000000000000000000010000000001000000000000000000010000000000000000010001000000000000100000100000010000000000000000000000001000100000000000000000000000000000000000000000000000000000001000100000000010000000000000000000001000000000000000000000000000',
            'd&c yellow #7': '00000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000100000000010000000000000000000000000000000110000000000000000010000000100000110000000001000000000000000000000000101000000001000000000000000000001000000000000010000000000000000000000000000010001000000100000010001000000000000100010100000010000000000000000000000000000000000000000000001000000000000000001010000010000000000000000100000000000000010000000000100000000000000000000000000000000',
            'd&c yellow #8': '00000000000000000000000000000000100000000000000000000000000000001000100000000000000000000000001000000000000000000000001001000000000010000010000010000000000000000000000010000001000000001000010010000110001100000001001000000000000000010000000000000000100000000000000000000001100000000000000000000001000000000000000000100000000000000000010001000000000100001100100000010000000000000000010000000000000000000000001000000000000100010000000010100000000001000000000100000000100000001000000000100000000000000000000000000000',
            'd&c yellow #11': '00000000000000000000000000000000000000000000000000000000000000011000000001000000000000000000000000000000000000000000000000000000000000000010000001010000000000000000000000000001000000000000100000000000000100000000101000000000000000000000000000000000000000000000000000000000000010000000000001000000000000000000000000100001000000000000000001000000000000001000100000001000000000000010000001000000000000000000000000000001000000000001000000000000000000000000000000000000000010001000001000000000000000000000000000010000',
            'd&c orange #4': '00000000000000000000000000000000000001000000000100000000000000011010000100000000100000000000000000000000001000000010000000000000010000000010000010000000000000000000000000000001000000000000010000000000001100000000011000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000100000000011000001000000010001000000000000100000100000000001000000000000000000000000000000000000000000000000000100000000000000000000000000000001100010000000000000000000000100000000000000000000000000000000',
            'd&c orange #10': '01000000000000010000000000000000000010000000000000000000000000001010001100001000000010000000000000000000000000000000000000000000000000000010000011000100000000001000010000000000000100000000000001000000000000000001001000000000000000000100000000000000100000000010000000000010001000000000000001000011001000000000100000100000000000001000000101000000001000000000100000010000010000000000010000000000000000000000000000000000000000000000000000011000000010000001000000001000000001000000000000000000000000000000000000000000',
            'd&c orange #11': '01000000000000000000000000000000000010000000000000000000000000001010000000001000000010000000000000000000000000000000000000000000000000000010000010000000000000000000010000000001000000000000000000000000000000000000001000000000000000000100000000000001000000000010000000000000001000000000000001000001001000000000000000100000000000001000000001000000000000001000100000010000010000000000010000000000000000000000000000000000000000001000000000001000000010000000000000001000001000001000000000000000000000000000000000000000',
        }

        return bit_vector