from django import forms

class FilterForm(forms.Form):
    assignee = forms.CharField(required=False)
    include_viewed = forms.BooleanField(required=False)


class CheckboxForm(forms.Form):
    def __init__(self,truth):
        super().__init__()
        self.fields['election_conspiracies'] = forms.BooleanField(required = False, initial=truth.ElectionConspiracies == 'x')
        self.fields['election_corruption'] = forms.BooleanField(required = False, initial=truth.ElectionCorruption == 'x')
        self.fields['fedsurrection'] = forms.BooleanField(required = False, initial=truth.Fedsurrection == 'x')
        self.fields['constitution_threat'] = forms.BooleanField(required = False, initial=truth.ConstitutionThreat == 'x')
        self.fields['praising_dictators'] = forms.BooleanField(required = False, initial=truth.PraisingDictators == 'x')
        self.fields['attacking_media'] = forms.BooleanField(required = False, initial=truth.AttackingMedia == 'x')
        self.fields['violence'] = forms.BooleanField(required = False, initial=truth.Violence == 'x')
        self.fields['vulnerable_communities'] = forms.BooleanField(required = False, initial=truth.VulnerableCommunities == 'x')
        self.fields['existential_threat'] = forms.BooleanField(required = False, initial=truth.ExistentialThreat == 'x')
        self.fields['politicizing_institutions'] = forms.BooleanField(required = False, initial=truth.PoliticizingInstitutions == 'x')
        self.fields['weaponizing_institutions'] = forms.BooleanField(required = False, initial=truth.WeaponizingInstitutions == 'x')
        self.fields['pressuring_courts'] = forms.BooleanField(required = False, initial=truth.PressuringCourts == 'x')
        self.fields['weaponizing_military'] = forms.BooleanField(required = False, initial=truth.WeaponizingMilitary == 'x')
        self.fields['abusing_power'] = forms.BooleanField(required = False, initial=truth.AbusingPower == 'x')
        self.fields['stay_in_office'] = forms.BooleanField(required = False, initial=truth.StayinOffice == 'x')
        self.fields['targeting_opponents'] = forms.BooleanField(required = False, initial=truth.TargetingOpponents == 'x')

    election_conspiracies = forms.BooleanField(required=False)
    election_corruption = forms.BooleanField(required=False)
    fedsurrection = forms.BooleanField(required=False)
    constitution_threat = forms.BooleanField(required=False)
    praising_dictators = forms.BooleanField(required=False)
    attacking_media = forms.BooleanField(required=False)
    violence = forms.BooleanField(required=False)
    vulnerable_communities = forms.BooleanField(required=False)
    existential_threat = forms.BooleanField(required=False)
    politicizing_institutions = forms.BooleanField(required=False)
    weaponizing_institutions = forms.BooleanField(required=False)
    pressuring_courts = forms.BooleanField(required=False)
    weaponizing_military = forms.BooleanField(required=False)
    abusing_power = forms.BooleanField(required=False)
    stay_in_office = forms.BooleanField(required=False)
    targeting_opponents = forms.BooleanField(required=False)

    viewed = forms.BooleanField(required=False, initial=True)