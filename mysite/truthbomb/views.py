from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import TruthSocial
from .forms import CheckboxForm, NameForm, ElectionsForm
from django.db.models import Q

def home(request):
    return render(request, "truthbomb/home.html",{
        "form" : NameForm()})

def index(request):
    latest_truth_list = TruthSocial.objects.all()
    if 'initials' in request.session:
        initials = request.session['initials']
        latest_truth_list = TruthSocial.objects.filter(viewed__exact = None)
        latest_truth_list = latest_truth_list.filter(assignee = initials)
    if 'topic' in request.session:
        if request.session['topic'] == 'jan6':
            latest_truth_list = latest_truth_list.filter(~Q(Fedsurrection=None))
        elif request.session['topic'] == 'power':
            latest_truth_list = latest_truth_list.filter(~Q(AbusingPower=None) | ~Q(WeaponizingInstitutions=None))
        elif request.session['topic'] == 'elections':
            latest_truth_list = TruthSocial.objects.filter(~Q(ElectionConspiracies = None))
    number_of_records = latest_truth_list.count()
    context = {"latest_truth_list": latest_truth_list, 'number_of_records': number_of_records, }
    return render(request, "truthbomb/index.html", context)

def skip(request, id):
    truth = TruthSocial.objects.get(pk=id)
    truth.viewed = None
    truth.save()
    return HttpResponseRedirect(reverse("truthbomb:index"))

def index_viewed(request):
    latest_truth_list = TruthSocial.objects.filter(viewed__exact = 'x')
    context = {"latest_truth_list": latest_truth_list}
    return render(request, "truthbomb/index.html", context)

def detail(request, id):
    try:
        truth = TruthSocial.objects.get(pk=id)
    except TruthSocial.DoesNotExist:
        raise Http404("Truth does not exist")
    embed_link = truth.url.replace("'", "") + "/embed"
    print(embed_link)
    if 'initials' in request.session:
        context = { "truth": truth, "embed_link": embed_link, "form" : CheckboxForm(truth=truth)}
    if 'topic' in request.session:
        context = { "truth": truth, "embed_link": embed_link, "form" : ElectionsForm(truth=truth)}
    return render(request, "truthbomb/detail.html", context)    

def submit(request, id):
    truth = get_object_or_404(TruthSocial, pk=id)
    if request.POST.get('election_conspiracies', 'off') == 'on' :
        truth.ElectionConspiracies = 'x'
    else :
        truth.ElectionConspiracies = None

    if request.POST.get('election_corruption', 'off') == 'on' :
        truth.ElectionCorruption = 'x'
    else :
        truth.ElectionCorruption = None

    if request.POST.get('fedsurrection', 'off') == 'on' :
        truth.Fedsurrection = 'x'
    else :
        truth.Fedsurrection = None

    if request.POST.get('constitution_threat', 'off') == 'on' :
        truth.ConstitutionThreat = 'x'
    else :
        truth.ConstitutionThreat = None

    if request.POST.get('praising_dictators', 'off') == 'on' :
        truth.PraisingDictators = 'x'
    else :
        truth.PraisingDictators = None

    if request.POST.get('attacking_media', 'off') == 'on' :
        truth.AttackingMedia = 'x'
    else :
        truth.AttackingMedia = None

    if request.POST.get('violence', 'off') == 'on' :
        truth.Violence = 'x'
    else :
        truth.Violence = None

    if request.POST.get('vulnerable_communities', 'off') == 'on' :
        truth.VulnerableCommunities = 'x'
    else :
        truth.VulnerableCommunities = None

    if request.POST.get('existential_threat', 'off') == 'on' :
        truth.ExistentialThreat = 'x'
    else :
        truth.ExistentialThreat = None

    if request.POST.get('politicizing_institutions', 'off') == 'on' :
        truth.PoliticizingInstitutions = 'x'
    else :
        truth.PoliticizingInstitutions = None

    if request.POST.get('weaponizing_institutions', 'off') == 'on' :
        truth.WeaponizingInstitutions = 'x'
    else :
        truth.WeaponizingInstitutions = None

    if request.POST.get('pressuring_courts', 'off') == 'on' :
        truth.PressuringCourts = 'x'
    else :
        truth.PressuringCourts = None

    if request.POST.get('weaponizing_military', 'off') == 'on' :
        truth.WeaponizingMilitary = 'x'
    else :
        truth.WeaponizingMilitary = None

    if request.POST.get('abusing_power', 'off') == 'on' :
        truth.AbusingPower = 'x'
    else :
        truth.AbusingPower = None

    if request.POST.get('stay_in_office', 'off') == 'on' :
        truth.StayinOffice = 'x'
    else :
        truth.StayinOffice = None

    if request.POST.get('targeting_opponents', 'off') == 'on' :
        truth.TargetingOpponents = 'x'
    else :
        truth.TargetingOpponents = None

    # VIEWED
    if request.POST.get('viewed', 'off') == 'on' :
        truth.viewed = 'x'
    else :
        truth.viewed = None


    truth.save()
    return HttpResponseRedirect(reverse("truthbomb:index"))

def skip(request, id):
    truth = TruthSocial.objects.get(pk=id)
    truth.viewed = None
    truth.save()
    return HttpResponseRedirect(reverse("truthbomb:index"))


def submit_topic(request):
    latest_truth_list = TruthSocial.objects.all()
    if request.POST.get('election_conspiracies', 'off') == 'on' :
        latest_truth_list = TruthSocial.objects.filter(~Q(ElectionConspiracies = None))
        request.session['topic'] = 'elections'
    elif request.POST.get('abusing_power', 'off') == 'on' :
        latest_truth_list = TruthSocial.objects.filter(~Q(AbusingPower=None) | ~Q(WeaponizingInstitutions=None))
        request.session['topic'] = 'power'
    elif request.POST.get('jan6', 'off') == 'on' :
        latest_truth_list = TruthSocial.objects.filter(~Q(Fedsurrection=None))
        request.session['topic'] = 'jan6'
    if 'initials' in request.session:
        del request.session['initials']
    number_of_records = latest_truth_list.count()
    context = {"latest_truth_list": latest_truth_list, 'number_of_records': number_of_records }
    return render(request, "truthbomb/index.html", context)

def skip_topic(request, id):
    truth = TruthSocial.objects.get(pk=id)
    truth.viewed = None
    truth.save()
    return HttpResponseRedirect(reverse("truthbomb:index_topic"))

def submit_initials(request):
    latest_truth_list = TruthSocial.objects.all()
    if request.POST.get('fname') is not None and request.POST.get('fname') != '':
        initials = request.POST.get('fname')
        latest_truth_list = TruthSocial.objects.filter(viewed__exact = None)
        latest_truth_list = latest_truth_list.filter(assignee = initials)
        request.session['initials'] = initials
    if 'topic' in request.session:
        del request.session["topic"]
    number_of_records = latest_truth_list.count()
    context = {"latest_truth_list": latest_truth_list, 'number_of_records': number_of_records}
    return render(request, "truthbomb/index.html", context)


def detailtopics(request, id):
    try:
        truth = TruthSocial.objects.get(pk=id)
    except TruthSocial.DoesNotExist:
        raise Http404("Truth does not exist")

    embed_link = truth.url.replace("'", "") + "/embed"
    print(embed_link)
    return render(request, "truthbomb/detailtopics.html", {
        "truth": truth, 
        "embed_link": embed_link,
        "form" : CheckboxForm(truth = truth)
    })   


