import FWCore.ParameterSet.Config as cms


jetKinematics = cms.PSet(
    pt = cms.string('pt() > 30.0'),
    eta = cms.string('abs(eta()) < 2.4'),
    phi = cms.string('abs(phi()) < 3.2')
    )

zjj = cms.PSet(
#    mass = cms.string('mass() >= 60 && mass() < 130'),
#    mass = cms.string('mass() >= 100 && mass() < 160'),
    mass = cms.string('mass() >= 50 && mass() < 140'),
)
isSignal = cms.PSet(
    mass = cms.string('mass() >= 110 && mass() < 140'),
)
isSideband = cms.PSet(
    mass = cms.string('(mass() >= 50 && mass() < 70)'),
)
isWSignal = cms.PSet(
#    mass = cms.string('mass() >= 110 && mass() < 135'),
    mass = cms.string('mass() >= 110 && mass() < 140'),
)
isWSideband = cms.PSet(
    mass = cms.string('(mass() >= 40 && mass() < 65 )'),
)

isFullRange = cms.PSet(
#        mass = cms.string('(mass() >= 40 && mass() < 65)||(mass() >= 110 && mass() < 135) '),
        mass = cms.string('(mass() >= 40 && mass() < 65)||(mass() >= 110 && mass() < 140) '),
)

### used for merged jet topology
mergedJetKinematics = cms.PSet(
    pt = cms.string('pt() > 80.0'),
    eta = cms.string('abs(eta()) < 2.4'),
    phi = cms.string('abs(phi()) < 3.2'),
    prunedMass = cms.string('prunedMass()>0.0')
    #prunedMass = cms.string('prunedMass()>40.0&&prunedMass()<130.0')
###    prunedMass = cms.string('prunedMass()>0.0&&prunedMass()<999.0')
    )

mergedJetVTagging = cms.PSet(
    qjet = cms.string('qjet() < 999.0 '),
    nsubjettiness = cms.string('ntau21() < 999.0 '),
    mdrop = cms.string('mdrop()<999.0')
    )

isMergedSignal = cms.PSet(
    prunedMass = cms.string('prunedMass()>70.0 && prunedMass()<110.0')
    )

isMergedSideband = cms.PSet(
    prunedMass = cms.string('(prunedMass()>50.0&&prunedMass()<70.0) || (prunedMass()>110.0&&prunedMass()<130.0)')
    )

isMergedWSignal = cms.PSet(
#    prunedMass = cms.string('prunedMass()>110.0 && prunedMass()<135.0')
    prunedMass = cms.string('prunedMass()>110.0 && prunedMass()<140.0')
    )

isMergedWSideband = cms.PSet(
    prunedMass = cms.string('prunedMass()>40.0&&prunedMass()<65.0')
    )
isMergedFullRange  = cms.PSet(
	prunedMass = cms.string('prunedMass()>0.0')
	)



