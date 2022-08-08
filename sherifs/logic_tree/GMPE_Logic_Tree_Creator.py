# -*- coding: utf-8 -*-
"""SHERIFS
Seismic Hazard and Earthquake Rates In Fault Systems

Version 1.0 


This code create a source logic tree for OQ calculation

@author: Thomas Chartier
"""
import os
import sys

path_actuel = os.path.dirname(os.path.abspath(__file__))
path_lib = path_actuel + '/lib'
sys.path.append(path_lib)
import GMPE_LT_GF
#import tkinter as tk
#from tkinter import ttk


class GMPE_Logic_Tree_Creator:

    def __init__(self, Run_Name, Domain_in_model):
        self.Run_Name = Run_Name
        self.Domain_in_model = Domain_in_model
        self.initialize()

    def initialize(self):
        if not os.path.exists(str(self.Run_Name) + '/GMPE_Logic_tree.xml'):
            #####################################################
            #######   open the graphical interface   ############
            #####################################################
            self.get_available_GMPE()
            GMPE_LT = GMPE_LT_GF.GMPE_lt(self.available_GMPE,
                                         self.Domain_in_model, self.Run_Name)

    def get_available_GMPE(self):  #list of available GMPE in OpenQuake 1.9
        self.available_GMPE = [
            'AbrahamsonEtAl2014', 'AbrahamsonEtAl2014NSHMPLower',
            'AbrahamsonEtAl2014NSHMPMean', 'AbrahamsonEtAl2014NSHMPUpper',
            'AbrahamsonEtAl2014RegCHN', 'AbrahamsonEtAl2014RegJPN',
            'AbrahamsonEtAl2014RegTWN', 'AbrahamsonEtAl2015SInter',
            'AbrahamsonEtAl2015SInterHigh', 'AbrahamsonEtAl2015SInterLow',
            'AbrahamsonEtAl2015SSlab', 'AbrahamsonEtAl2015SSlabHigh',
            'AbrahamsonEtAl2015SSlabLow', 'AbrahamsonSilva1997',
            'AbrahamsonSilva2008', 'AkkarBommer2010', 'AkkarBommer2010SWISS01',
            'AkkarBommer2010SWISS04', 'AkkarBommer2010SWISS08',
            'AkkarCagnan2010', 'AkkarEtAl2013', 'AkkarEtAlRepi2014',
            'AkkarEtAlRhyp2014', 'AkkarEtAlRjb2014', 'Allen2012',
            'AllenEtAl2012', 'AllenEtAl2012Rhypo', 'Atkinson2015',
            'AtkinsonBoore1995GSCBest', 'AtkinsonBoore1995GSCLowerLimit',
            'AtkinsonBoore1995GSCUpperLimit', 'AtkinsonBoore2003SInter',
            'AtkinsonBoore2003SInterNSHMP2008', 'AtkinsonBoore2003SSlab',
            'AtkinsonBoore2003SSlabCascadia',
            'AtkinsonBoore2003SSlabCascadiaNSHMP2008',
            'AtkinsonBoore2003SSlabJapan',
            'AtkinsonBoore2003SSlabJapanNSHMP2008',
            'AtkinsonBoore2003SSlabNSHMP2008', 'AtkinsonBoore2006',
            'AtkinsonBoore2006MblgAB1987bar140NSHMP2008',
            'AtkinsonBoore2006MblgAB1987bar200NSHMP2008',
            'AtkinsonBoore2006MblgJ1996bar140NSHMP2008',
            'AtkinsonBoore2006MblgJ1996bar200NSHMP2008',
            'AtkinsonBoore2006Modified2011',
            'AtkinsonBoore2006Mwbar140NSHMP2008',
            'AtkinsonBoore2006Mwbar200NSHMP2008', 'AtkinsonMacias2009',
            'BergeThierryEtAl2003SIGMA', 'BindiEtAl2011', 'BindiEtAl2014Rhyp',
            'BindiEtAl2014RhypEC8', 'BindiEtAl2014RhypEC8NoSOF',
            'BindiEtAl2014Rjb', 'BindiEtAl2014RjbEC8',
            'BindiEtAl2014RjbEC8NoSOF', 'BooreAtkinson2008',
            'BooreAtkinson2011', 'BooreEtAl1993GSCBest',
            'BooreEtAl1993GSCLowerLimit', 'BooreEtAl1993GSCUpperLimit',
            'BooreEtAl1997ArbitraryHorizontal',
            'BooreEtAl1997ArbitraryHorizontalUnspecified',
            'BooreEtAl1997GeometricMean',
            'BooreEtAl1997GeometricMeanUnspecified', 'BooreEtAl2014',
            'BooreEtAl2014CaliforniaBasin', 'BooreEtAl2014CaliforniaBasinNoSOF',
            'BooreEtAl2014HighQ', 'BooreEtAl2014HighQCaliforniaBasin',
            'BooreEtAl2014HighQCaliforniaBasinNoSOF',
            'BooreEtAl2014HighQJapanBasin', 'BooreEtAl2014HighQJapanBasinNoSOF',
            'BooreEtAl2014HighQNoSOF', 'BooreEtAl2014JapanBasin',
            'BooreEtAl2014JapanBasinNoSOF', 'BooreEtAl2014LowQ',
            'BooreEtAl2014LowQCaliforniaBasin',
            'BooreEtAl2014LowQCaliforniaBasinNoSOF',
            'BooreEtAl2014LowQJapanBasin', 'BooreEtAl2014LowQJapanBasinNoSOF',
            'BooreEtAl2014LowQNoSOF', 'BooreEtAl2014NSHMPLower',
            'BooreEtAl2014NSHMPMean', 'BooreEtAl2014NSHMPUpper',
            'BooreEtAl2014NoSOF', 'Bradley2013', 'Bradley2013Volc',
            'Campbell2003', 'Campbell2003MblgAB1987NSHMP2008',
            'Campbell2003MblgJ1996NSHMP2008', 'Campbell2003MwNSHMP2008',
            'Campbell2003SHARE', 'CampbellBozorgnia2003NSHMP2007',
            'CampbellBozorgnia2008', 'CampbellBozorgnia2008Arbitrary',
            'CampbellBozorgnia2014', 'CampbellBozorgnia2014HighQ',
            'CampbellBozorgnia2014HighQJapanSite',
            'CampbellBozorgnia2014JapanSite', 'CampbellBozorgnia2014LowQ',
            'CampbellBozorgnia2014LowQJapanSite',
            'CampbellBozorgnia2014NSHMPLower', 'CampbellBozorgnia2014NSHMPMean',
            'CampbellBozorgnia2014NSHMPUpper', 'CauzziEtAl2014',
            'CauzziEtAl2014Eurocode8', 'CauzziEtAl2014Eurocode8NoSOF',
            'CauzziEtAl2014FixedVs30', 'CauzziEtAl2014FixedVs30NoSOF',
            'CauzziEtAl2014NoSOF', 'CauzziFaccioli2008',
            'CauzziFaccioli2008SWISS01', 'CauzziFaccioli2008SWISS04',
            'CauzziFaccioli2008SWISS08', 'ChiouYoungs2008',
            'ChiouYoungs2008SWISS01', 'ChiouYoungs2008SWISS04',
            'ChiouYoungs2008SWISS06', 'ChiouYoungs2014',
            'ChiouYoungs2014NSHMPLower', 'ChiouYoungs2014NSHMPMean',
            'ChiouYoungs2014NSHMPUpper', 'ChiouYoungs2014NearFaultEffect',
            'ChiouYoungs2014PEER', 'ClimentEtAl1994',
            'ConvertitoEtAl2012Geysers', 'DostEtAl2004',
            'DostEtAl2004BommerAdaptation',
            'DouglasEtAl2013StochasticSD001Q1800K005',
            'DouglasEtAl2013StochasticSD001Q1800K020',
            'DouglasEtAl2013StochasticSD001Q1800K040',
            'DouglasEtAl2013StochasticSD001Q1800K060',
            'DouglasEtAl2013StochasticSD001Q200K005',
            'DouglasEtAl2013StochasticSD001Q200K020',
            'DouglasEtAl2013StochasticSD001Q200K040',
            'DouglasEtAl2013StochasticSD001Q200K060',
            'DouglasEtAl2013StochasticSD001Q600K005',
            'DouglasEtAl2013StochasticSD001Q600K020',
            'DouglasEtAl2013StochasticSD001Q600K040',
            'DouglasEtAl2013StochasticSD001Q600K060',
            'DouglasEtAl2013StochasticSD010Q1800K005',
            'DouglasEtAl2013StochasticSD010Q1800K020',
            'DouglasEtAl2013StochasticSD010Q1800K040',
            'DouglasEtAl2013StochasticSD010Q1800K060',
            'DouglasEtAl2013StochasticSD010Q200K005',
            'DouglasEtAl2013StochasticSD010Q200K020',
            'DouglasEtAl2013StochasticSD010Q200K040',
            'DouglasEtAl2013StochasticSD010Q200K060',
            'DouglasEtAl2013StochasticSD010Q600K005',
            'DouglasEtAl2013StochasticSD010Q600K020',
            'DouglasEtAl2013StochasticSD010Q600K040',
            'DouglasEtAl2013StochasticSD010Q600K060',
            'DouglasEtAl2013StochasticSD100Q1800K005',
            'DouglasEtAl2013StochasticSD100Q1800K020',
            'DouglasEtAl2013StochasticSD100Q1800K040',
            'DouglasEtAl2013StochasticSD100Q1800K060',
            'DouglasEtAl2013StochasticSD100Q200K005',
            'DouglasEtAl2013StochasticSD100Q200K020',
            'DouglasEtAl2013StochasticSD100Q200K040',
            'DouglasEtAl2013StochasticSD100Q200K060',
            'DouglasEtAl2013StochasticSD100Q600K005',
            'DouglasEtAl2013StochasticSD100Q600K020',
            'DouglasEtAl2013StochasticSD100Q600K040',
            'DouglasEtAl2013StochasticSD100Q600K060', 'DowrickRhoades2005Asc',
            'DowrickRhoades2005SInter', 'DowrickRhoades2005SSlab',
            'DowrickRhoades2005Volc', 'DrouetBrazil2015',
            'DrouetBrazil2015withDepth', 'EdwardsFah2013Alpine10Bars',
            'EdwardsFah2013Alpine120Bars', 'EdwardsFah2013Alpine20Bars',
            'EdwardsFah2013Alpine30Bars', 'EdwardsFah2013Alpine50Bars',
            'EdwardsFah2013Alpine60Bars', 'EdwardsFah2013Alpine75Bars',
            'EdwardsFah2013Alpine90Bars', 'EdwardsFah2013Foreland10Bars',
            'EdwardsFah2013Foreland120Bars', 'EdwardsFah2013Foreland20Bars',
            'EdwardsFah2013Foreland30Bars', 'EdwardsFah2013Foreland50Bars',
            'EdwardsFah2013Foreland60Bars', 'EdwardsFah2013Foreland75Bars',
            'EdwardsFah2013Foreland90Bars', 'FaccioliEtAl2010',
            'FrankelEtAl1996MblgAB1987NSHMP2008',
            'FrankelEtAl1996MblgJ1996NSHMP2008', 'FrankelEtAl1996MwNSHMP2008',
            'FukushimaTanaka1990', 'FukushimaTanakaSite1990', 'GMPETable',
            'GarciaEtAl2005SSlab', 'GarciaEtAl2005SSlabVert',
            'Geomatrix1993SSlabNSHMP2008', 'GhofraniAtkinson2014',
            'GhofraniAtkinson2014Cascadia', 'GhofraniAtkinson2014CascadiaLower',
            'GhofraniAtkinson2014CascadiaUpper', 'GhofraniAtkinson2014Lower',
            'GhofraniAtkinson2014Upper', 'Gupta2010SSlab', 'Idriss2014',
            'Idriss2014NSHMPLower', 'Idriss2014NSHMPMean',
            'Idriss2014NSHMPUpper', 'Kanno2006Deep', 'Kanno2006Shallow',
            'Lin2009', 'Lin2009AdjustedSigma', 'LinLee2008SInter',
            'LinLee2008SSlab', 'McVerry2006Asc', 'McVerry2006SInter',
            'McVerry2006SSlab', 'McVerry2006Volc', 'MegawatiPan2010',
            'MontalvaEtAl2015SInter', 'MontalvaEtAl2015SSlab',
            'NathEtAl2012Lower', 'NathEtAl2012Upper', 'PezeshkEtAl2011',
            'RaghukanthIyengar2007', 'RaghukanthIyengar2007KoynaWarna',
            'RaghukanthIyengar2007Southern',
            'RaghukanthIyengar2007WesternCentral',
            'RietbrockEtAl2013MagDependent', 'RietbrockEtAl2013SelfSimilar',
            'SadighEtAl1997', 'SharmaEtAl2009', 'SiMidorikawa1999Asc',
            'SiMidorikawa1999SInter',
            'SiMidorikawa1999SInterNorthEastCorrection',
            'SiMidorikawa1999SInterSouthWestCorrection',
            'SiMidorikawa1999SSlab', 'SiMidorikawa1999SSlabNorthEastCorrection',
            'SiMidorikawa1999SSlabSouthWestCorrection',
            'SilvaEtAl2002MblgAB1987NSHMP2008',
            'SilvaEtAl2002MblgJ1996NSHMP2008', 'SilvaEtAl2002MwNSHMP2008',
            'SomervilleEtAl2001NSHMP2008', 'SomervilleEtAl2009NonCratonic',
            'SomervilleEtAl2009YilgarnCraton', 'TavakoliPezeshk2005',
            'TavakoliPezeshk2005MblgAB1987NSHMP2008',
            'TavakoliPezeshk2005MblgJ1996NSHMP2008',
            'TavakoliPezeshk2005MwNSHMP2008', 'ToroEtAl1997MblgNSHMP2008',
            'ToroEtAl1997MwNSHMP2008', 'ToroEtAl2002', 'ToroEtAl2002SHARE',
            'TusaLanger2015RepiBA08DE', 'TusaLanger2015RepiBA08SE',
            'TusaLanger2015RepiSP87DE', 'TusaLanger2015RepiSP87SE',
            'TusaLanger2015Rhypo', 'YoungsEtAl1997GSCSSlabBest',
            'YoungsEtAl1997GSCSSlabLowerLimit',
            'YoungsEtAl1997GSCSSlabUpperLimit', 'YoungsEtAl1997SInter',
            'YoungsEtAl1997SInterNSHMP2008', 'YoungsEtAl1997SSlab',
            'ZhaoEtAl2006Asc', 'ZhaoEtAl2006AscSWISS03',
            'ZhaoEtAl2006AscSWISS05', 'ZhaoEtAl2006AscSWISS08',
            'ZhaoEtAl2006SInter', 'ZhaoEtAl2006SInterNSHMP2008',
            'ZhaoEtAl2006SSlab'
        ]
