#!/usr/bin/env python3
#
# GlobalChem - FDA List Five
#
# -------------------------

class FDAListFive(object):

    def __init__(self):

        self.name = 'fda_list_five'

    @staticmethod
    def get_smiles():

        smiles = {
            'alumina': 'O=[Al]O[Al]=O',
            'aluminum powder': '[Al]',
            'annatto extract': 'CC(=CC=CC=C(C)C=CC=C(C)C=CC(=O)O)C=CC=C(C)C=CC(=O)O',
            'beta-carotene': 'CC1=C(C(CCC1)(C)C)C=CC(=CC=CC(=CC=CC=C(C)C=CC=C(C)C=CC2=C(CCCC2(C)C)C)C)C',
            'bismuth oxychloride': 'O=[Bi].Cl',
            'bronze powder': '[Cu].[Sn]',
            'calcium carbonate': 'C(=O)([O-])[O-].[Ca+2]',
            'canthaxanthin': 'CC1=C(C(CCC1=O)(C)C)C=CC(=CC=CC(=CC=CC=C(C)C=CC=C(C)C=CC2=C(C(=O)CCC2(C)C)C)C)C',
            'caramel': '*',
            'carmine': 'CC1=C2C(=CC(=C1C(=O)O)O)C(=O)C3=C(C2=O)C(=C(C(=C3O)O)C4C(C(C(C(O4)CO)O)O)O)O',
            'chlorophyllin, copper complex': 'CCC1=C(C2=NC1=CC3=C(C(=C([O-])[O-])C(=N3)C(=C4C(C(C(=CC5=NC(=C2)C(=C5C)C=C)N4)C)CCC(=O)O)CC(=O)O)C)C.[Cu+2]',
            'chromium hydroxide, green': 'O.O.[O-2].[O-2].[O-2].[Cr+3].[Cr+3]',
            'chromium oxides greens': 'O=[Cr]O[Cr]=O',
            'cochineal extract': 'CC1=C2C(=CC(=C1C(=O)O)O)C(=O)C3=C(C2=O)C(=C(C(=C3O)O)C4C(C(C(C(O4)CO)O)O)O)O',
            'copper, metallic powder': '[Cu]',
            'potassium sodium copper chlorophyllin': 'CCC1=C(C2=NC1=CC3=C(C(=C([N-]3)C(=C4C(C(C(=N4)C=C5C(=C(C(=C2)[N-]5)C=C)C)C)CCC(=O)[O-])CC(=O)[O-])C(=O)[O-])C)C.[Na+].[Na+].[Na+].[Cu+2]',
            'dihydroxyacetone': 'C(C(=O)CO)O',
            'ferric ammonium ferrocyanide': '[C-]#N.[C-]#N.[C-]#N.[C-]#N.[C-]#N.[C-]#N.[NH4+].[Fe+2].[Fe+3]',
            'ferric ferrocyanide': '[C-]#N.[C-]#N.[C-]#N.[C-]#N.[C-]#N.[C-]#N.[Fe+3].[Fe+3]',
            'guanine': 'C1=NC2=C(N1)C(=O)NC(=N2)N',
            'mica': '[O-2].O=[Al]O[Al]=O.O=[Si]=O.[K+].[K+]',
            'mica-based pearlescent pigment': '*',
            'pyrophyllite': 'O[Si](=O)[O-].O[Si](=O)[O-].[Al+2]',
            'synthetic iron oxide': 'O=[Fe]O[Fe]=O',
            'talc': 'O.O=[Mg].O=[Mg].O=[Mg].O=[Si]=O.O=[Si]=O.O=[Si]=O.O=[Si]=O',
            'titanium dioxide': 'O=[Ti]=O',
            'zinc oxide': 'O=[Zn]',
        }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {
            'alumina': '[#8]=[Al]-[#8]-[Al]=[#8]',
            'aluminum powder': '[Al]',
            'annatto extract': '[#6]-[#6](=[#6]-[#6]=[#6]-[#6]=[#6](-[#6])-[#6]=[#6]-[#6]=[#6](-[#6])-[#6]=[#6]-[#6](=[#8])-[#8])-[#6]=[#6]-[#6]=[#6](-[#6])-[#6]=[#6]-[#6](=[#8])-[#8]',
            'beta-carotene': '[#6]-[#6]1=[#6](-[#6](-[#6]-[#6]-[#6]-1)(-[#6])-[#6])-[#6]=[#6]-[#6](=[#6]-[#6]=[#6]-[#6](=[#6]-[#6]=[#6]-[#6]=[#6](-[#6])-[#6]=[#6]-[#6]=[#6](-[#6])-[#6]=[#6]-[#6]1=[#6](-[#6]-[#6]-[#6]-[#6]-1(-[#6])-[#6])-[#6])-[#6])-[#6]',
            'bismuth oxychloride': '[#8]=[Bi].[#17]',
            'bronze powder': '[Cu].[Sn]',
            'calcium carbonate': '[#6](=[#8])(-[#8-])-[#8-].[Ca+2]',
            'canthaxanthin': '[#6]-[#6]1=[#6](-[#6](-[#6]-[#6]-[#6]-1=[#8])(-[#6])-[#6])-[#6]=[#6]-[#6](=[#6]-[#6]=[#6]-[#6](=[#6]-[#6]=[#6]-[#6]=[#6](-[#6])-[#6]=[#6]-[#6]=[#6](-[#6])-[#6]=[#6]-[#6]1=[#6](-[#6](=[#8])-[#6]-[#6]-[#6]-1(-[#6])-[#6])-[#6])-[#6])-[#6]',
            'caramel': '[#0]',
            'carmine': '[#6]-[#6]1:[#6]2:[#6](:[#6]:[#6](:[#6]:1-[#6](=[#8])-[#8])-[#8])-[#6](=[#8])-[#6]1:[#6](-[#6]-2=[#8]):[#6](:[#6](:[#6](:[#6]:1-[#8])-[#8])-[#6]1-[#6](-[#6](-[#6](-[#6](-[#8]-1)-[#6]-[#8])-[#8])-[#8])-[#8])-[#8]',
            'chlorophyllin, copper complex': '[#6]-[#6]-[#6]1=[#6](-[#6]2=[#7]-[#6]-1=[#6]-[#6]1=[#6](-[#6](=[#6](-[#8-])-[#8-])-[#6](=[#7]-1)-[#6](=[#6]1-[#6](-[#6](-[#6](=[#6]-[#6]3=[#7]-[#6](=[#6]-2)-[#6](=[#6]-3-[#6])-[#6]=[#6])-[#7]-1)-[#6])-[#6]-[#6]-[#6](=[#8])-[#8])-[#6]-[#6](=[#8])-[#8])-[#6])-[#6].[Cu+2]',
            'chromium hydroxide, green': '[#8].[#8].[#8-2].[#8-2].[#8-2].[Cr+3].[Cr+3]',
            'chromium oxides greens': '[#8]=[Cr]-[#8]-[Cr]=[#8]',
            'cochineal extract': '[#6]-[#6]1:[#6]2:[#6](:[#6]:[#6](:[#6]:1-[#6](=[#8])-[#8])-[#8])-[#6](=[#8])-[#6]1:[#6](-[#6]-2=[#8]):[#6](:[#6](:[#6](:[#6]:1-[#8])-[#8])-[#6]1-[#6](-[#6](-[#6](-[#6](-[#8]-1)-[#6]-[#8])-[#8])-[#8])-[#8])-[#8]',
            'copper, metallic powder': '[Cu]',
            'potassium sodium copper chlorophyllin': '[#6]-[#6]-[#6]1=[#6](-[#6]2:[#7]:[#6]-1:[#6]:[#6]1:[#6](:[#6](:[#6](:[#7-]:1):[#6](:[#6]1-[#6](-[#6](-[#6](:[#7]:1):[#6]:[#6]1:[#6](:[#6](:[#6](:[#6]:2):[#7-]:1)-[#6]=[#6])-[#6])-[#6])-[#6]-[#6]-[#6](=[#8])-[#8-])-[#6]-[#6](=[#8])-[#8-])-[#6](=[#8])-[#8-])-[#6])-[#6].[Na+].[Na+].[Na+].[Cu+2]',
            'dihydroxyacetone': '[#6](-[#6](=[#8])-[#6]-[#8])-[#8]',
            'ferric ammonium ferrocyanide': '[#6-]#[#7].[#6-]#[#7].[#6-]#[#7].[#6-]#[#7].[#6-]#[#7].[#6-]#[#7].[#7H4+].[Fe+2].[Fe+3]',
            'ferric ferrocyanide': '[#6-]#[#7].[#6-]#[#7].[#6-]#[#7].[#6-]#[#7].[#6-]#[#7].[#6-]#[#7].[Fe+3].[Fe+3]',
            'guanine': '[#6]1:[#7]:[#6]2:[#6](:[#7H]:1):[#6](=[#8]):[#7H]:[#6](:[#7]:2)-[#7]',
            'mica': '[#8-2].[#8]=[Al]-[#8]-[Al]=[#8].[#8]=[Si]=[#8].[K+].[K+]',
            'mica-based pearlescent pigment': '[#0]',
            'pyrophyllite': '[#8]-[Si](=[#8])-[#8-].[#8]-[Si](=[#8])-[#8-].[Al+2]',
            'synthetic iron oxide': '[#8]=[Fe]-[#8]-[Fe]=[#8]',
            'talc': '[#8].[#8]=[Mg].[#8]=[Mg].[#8]=[Mg].[#8]=[Si]=[#8].[#8]=[Si]=[#8].[#8]=[Si]=[#8].[#8]=[Si]=[#8]',
            'titanium dioxide': '[#8]=[Ti]=[#8]',
            'zinc oxide': '[#8]=[Zn]',
        }

        return smarts

    @staticmethod
    def get_bit_vector():

        bit_vector = {
            'alumina': '00000000000000000000000000000000000000000000100000000000000000000000000000000000000100000000000000000000000000000000001000000000000000000010000000000000000000000000000000000001000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000',
            'aluminum powder': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'annatto extract': '00000000000000000000000000000001010000000000000000000001000000000000000000000000000000000010000000000000000000000000000000000000000000000010000000000000000000100000000000000100000000100000000000000000000000100000000000001000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000100000000000000000000000000000001000000000010000000000000000000000000000000100000000000000000000000000100000000000001001000',
            'beta-carotene': '00001000000000000000000000000001010010001000000000000001000000000000000000000000000000000010000000000000001000000000000000000000001000000010000000000000000000000000000000000100000000100010000000000000001000100000000000000000000000000000000000000000001000000001000010000000000000000000000000010001000000000000000000000000000101000000000000000000000000000000100000000000000000000000000000000000000000000000000000000010000011000000000010000000010010000000000000000000000000000000000000000000000100000000100001000000',
            'bismuth oxychloride': '00100000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'bronze powder': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'calcium carbonate': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000001000000000000000001100000000000000000000000000000000000000000000000000000000000000000000000000000000100000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'canthaxanthin': '00000000000000000000000000000001010010000000000000000001001000000000010000000000000000000010000000000000001000000000000000000000000000000010000010000000000000000000000000000100000000100010000000000000001000100000000000000000000000000010000100000000001000000001000010000000000000000000000000000001000000000000000000100000000100000000100000000000000000000000100000000000000000000000000000000000000000000000000000000010000001000000000010000000010000000000100000000000000000000000000000000000000100000000100001000000',
            'caramel': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'carmine': '00000000000001000000000000000000011000000000000010000000000000001010000100110000100000000000000000100000000000001000000000000000000000000010000010000000000000100000000000000000000010000010000000000000001000000011000000000010000010100100000000000000000010000000000000100000000100000000000000000001000000000000100000110000000000000000000001010000000000001000100000010000000000000000010001000100000000000000000010000000000000000000000010000000000100000100100010000101000000000000000000000000101010000000000000010000',
            'chlorophyllin, copper complex': '00000000000001000000000000001000010010000001001000001000010000000000010010010000100010000010000000000010000001000000000010000000000000000010001000011000000000000100000000000000000100100010100000000010011100000000100000000000000100000000000001000000000000000000000100000000000100000000010010000011010001000110000000100000100001001001000001100010011000000000100000010010000000000010010000001100010000000010000000000001000000000000000000000010000000000100100000000000000000000001000000000000000000000000000000010000',
            'chromium hydroxide, green': '00000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'chromium oxides greens': '01000100000000000000000000010000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000010000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'cochineal extract': '00000000000001000000000000000000011000000000000010000000000000001010000100110000100000000000000000100000000000001000000000000000000000000010000010000000000000100000000000000000000010000010000000000000001000000011000000000010000010100100000000000000000010000000000000100000000100000000000000000001000000000000100000110000000000000000000001010000000000001000100000010000000000000000010001000100000000000000000010000000000000000000000010000000000100000100100010000101000000000000000000000000101010000000000000010000',
            'copper, metallic powder': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'potassium sodium copper chlorophyllin': '00000000000001000000000000001000110000001000000000100000000000010000010000100000100000000001000000000000010001000000000000100000000000000010001000000100000000000000000000000000010000100010010000000010001100010000001000000001000100000101000000000000100010000001000100000001010000000000110000000011000000010010000000000001100001000000000101010010000000110000100000010000000000000010010000000000000010000000000000000000000000000000100010000010000000000000000000000000010010000000100100000000000000000110000000010000',
            'dihydroxyacetone': '00000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000100000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000010000001000000000000000000000000000000000000000000000000001000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'ferric ammonium ferrocyanide': '00000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000001000000000000000000000100000000000000000000000000000000000000000000000000000000000000001',
            'ferric ferrocyanide': '00000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
            'guanine': '10000000000000000000000000000000000000000000000000010000000000000000000000000000000000001010000000000000000000000000000000000000000000000010000000010000000000000000000000000000000000000100000100000000010000000100000000000000000000000000001000000000000000000000000000000000000000000000000000000010000000000000000000110001001000000000001001000000000000000000100000000000000000000010000000000000000000000100000000000000000000000000100001000000000000000000000000000000000000000000100000000000000000000000000000101000',
            'mica': '10000000000000000000000000000000000000000000100000000000000000000000000000000100000100000000000000000000000000000000001000000000000000000010000000000000000000000000001000000001000000010000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000',
            'mica-based pearlescent pigment': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'pyrophyllite': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000001000000000000000000000000000010000000000000000000000000000000000000000000000001000000000000000000000000000000001000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000',
            'synthetic iron oxide': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000001000000000000000000010000000000000000000000000000000000000000000010000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000001100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000',
            'talc': '10000000000000000000000000000000000000000000000010000000000000000000000000000100000000000000000000000000000000000000001000000000000000000010000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'titanium dioxide': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000001000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'zinc oxide': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010010000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
        }

        return bit_vector