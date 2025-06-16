from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import (
    Nation, League, Club, Position, Player, PlayerStat,
    ListingStatus, TransferListing, BidStatus, Bid,
    TransactionType, Transaction, UserSquad, SquadPosition,
    SBCDifficulty, SBC, SBCReward, SBCRequirement
)
from .forms import (
    NationForm, LeagueForm, ClubForm, PositionForm, PlayerForm, PlayerStatForm,
    ListingStatusForm, TransferListingForm, BidStatusForm, BidForm,
    TransactionTypeForm, TransactionForm, UserSquadForm, SquadPositionForm,
    SBCDifficultyForm, SBCForm, SBCRewardForm, SBCRequirementForm, PlayerCreationForm,
    CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm, SellPlayerForm
)

from .models import CustomUser
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

import random
from django.utils import timezone


def info_view(request):
    return render(request, 'info.html')

# Регистрация
class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

# Вход
class UserLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'users/login.html'

# Выход
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# CRUD для пользователей
class UserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user_obj'

class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')




class NationListView(ListView):
    model = Nation
    template_name = 'nation/nation_list.html'
    context_object_name = 'nations'

class NationDetailView(DetailView):
    model = Nation
    template_name = 'nation/nation_detail.html'
    context_object_name = 'nation'

class NationCreateView(CreateView):
    model = Nation
    form_class = NationForm
    template_name = 'nation/nation_form.html'
    success_url = reverse_lazy('nation_list_view')

class NationUpdateView(UpdateView):
    model = Nation
    form_class = NationForm
    template_name = 'nation/nation_form.html'
    success_url = reverse_lazy('nation_list_view')

class NationDeleteView(DeleteView):
    model = Nation
    template_name = 'nation/nation_confirm_delete.html'
    success_url = reverse_lazy('nation_list_view')


class LeagueListView(ListView):
    model = League
    template_name = 'league/league_list.html'
    context_object_name = 'leagues'

class LeagueDetailView(DetailView):
    model = League
    template_name = 'league/league_detail.html'
    context_object_name = 'league'

class LeagueCreateView(CreateView):
    model = League
    form_class = LeagueForm
    template_name = 'league/league_form.html'
    success_url = reverse_lazy('league_list_view')

class LeagueUpdateView(UpdateView):
    model = League
    form_class = LeagueForm
    template_name = 'league/league_form.html'
    success_url = reverse_lazy('league_list_view')

class LeagueDeleteView(DeleteView):
    model = League
    template_name = 'league/league_confirm_delete.html'
    success_url = reverse_lazy('league_list_view')


class ClubListView(ListView):
    model = Club
    template_name = 'club/club_list.html'
    context_object_name = 'clubs'

class ClubDetailView(DetailView):
    model = Club
    template_name = 'club/club_detail.html'
    context_object_name = 'club'

class ClubCreateView(CreateView):
    model = Club
    form_class = ClubForm
    template_name = 'club/club_form.html'
    success_url = reverse_lazy('club_list_view')

class ClubUpdateView(UpdateView):
    model = Club
    form_class = ClubForm
    template_name = 'club/club_form.html'
    success_url = reverse_lazy('club_list_view')

class ClubDeleteView(DeleteView):
    model = Club
    template_name = 'club/club_confirm_delete.html'
    success_url = reverse_lazy('club_list_view')

class PositionListView(ListView):
    model = Position
    template_name = 'position/position_list.html'
    context_object_name = 'positions'

class PositionDetailView(DetailView):
    model = Position
    template_name = 'position/position_detail.html'
    context_object_name = 'position'

class PositionCreateView(CreateView):
    model = Position
    form_class = PositionForm
    template_name = 'position/position_form.html'
    success_url = reverse_lazy('position_list_view')

class PositionUpdateView(UpdateView):
    model = Position
    form_class = PositionForm
    template_name = 'position/position_form.html'
    success_url = reverse_lazy('position_list_view')

class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'position/position_confirm_delete.html'
    success_url = reverse_lazy('position_list_view')

# ListingStatus CRUD
class ListingStatusListView(ListView):
    model = ListingStatus
    template_name = 'listingstatus/listingstatus_list.html'
    context_object_name = 'statuses'

class ListingStatusCreateView(CreateView):
    model = ListingStatus
    form_class = ListingStatusForm
    template_name = 'listingstatus/listingstatus_form.html'
    success_url = reverse_lazy('listingstatus_list_view')

class ListingStatusUpdateView(UpdateView):
    model = ListingStatus
    form_class = ListingStatusForm
    template_name = 'listingstatus/listingstatus_form.html'
    success_url = reverse_lazy('listingstatus_list_view')

class ListingStatusDeleteView(DeleteView):
    model = ListingStatus
    template_name = 'listingstatus/listingstatus_confirm_delete.html'
    success_url = reverse_lazy('listingstatus_list_view')

# BidStatus CRUD
class BidStatusListView(ListView):
    model = BidStatus
    template_name = 'bidstatus/bidstatus_list.html'
    context_object_name = 'bidstatuses'

class BidStatusCreateView(CreateView):
    model = BidStatus
    form_class = BidStatusForm
    template_name = 'bidstatus/bidstatus_form.html'
    success_url = reverse_lazy('bidstatus_list_view')

class BidStatusUpdateView(UpdateView):
    model = BidStatus
    form_class = BidStatusForm
    template_name = 'bidstatus/bidstatus_form.html'
    success_url = reverse_lazy('bidstatus_list_view')

class BidStatusDeleteView(DeleteView):
    model = BidStatus
    template_name = 'bidstatus/bidstatus_confirm_delete.html'
    success_url = reverse_lazy('bidstatus_list_view')

# Player CRUD
class PlayerListView(ListView):
    model = Player
    template_name = 'player/player_list.html'
    context_object_name = 'players'

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player/player_detail.html'
    context_object_name = 'player'

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player/player_form.html'
    success_url = reverse_lazy('player_list_view')

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player/player_form.html'
    success_url = reverse_lazy('player_list_view')

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'player/player_confirm_delete.html'
    success_url = reverse_lazy('player_list_view')

class PlayerStatUpdateView(UpdateView):
    model = PlayerStat
    form_class = PlayerStatForm
    template_name = 'playerstat/playerstat_form.html'
    success_url = reverse_lazy('player_list_view')


class TransferListingListView(ListView):
    model = TransferListing
    template_name = 'transferlisting/transferlisting_list.html'
    context_object_name = 'listings'

class TransferListingDetailView(DetailView):
    model = TransferListing
    template_name = 'transferlisting/transferlisting_detail.html'
    context_object_name = 'listing'

class TransferListingCreateView(CreateView):
    model = TransferListing
    form_class = TransferListingForm
    template_name = 'transferlisting/transferlisting_form.html'
    success_url = reverse_lazy('listing_list_view')

class TransferListingUpdateView(UpdateView):
    model = TransferListing
    form_class = TransferListingForm
    template_name = 'transferlisting/transferlisting_form.html'
    success_url = reverse_lazy('listing_list_view')

class TransferListingDeleteView(DeleteView):
    model = TransferListing
    template_name = 'transferlisting/transferlisting_confirm_delete.html'
    success_url = reverse_lazy('listing_list_view')


class BidListView(ListView):
    model = Bid
    template_name = 'bid/bid_list.html'
    context_object_name = 'bids'

class BidCreateView(CreateView):
    model = Bid
    form_class = BidForm
    template_name = 'bid/bid_form.html'
    success_url = reverse_lazy('bid_list_view')

# TransactionType CRUD
class TransactionTypeListView(ListView):
    model = TransactionType
    template_name = 'transactiontype/transactiontype_list.html'
    context_object_name = 'transactiontypes'

class TransactionTypeCreateView(CreateView):
    model = TransactionType
    form_class = TransactionTypeForm
    template_name = 'transactiontype/transactiontype_form.html'
    success_url = reverse_lazy('transactiontype_list_view')

class TransactionTypeUpdateView(UpdateView):
    model = TransactionType
    form_class = TransactionTypeForm
    template_name = 'transactiontype/transactiontype_form.html'
    success_url = reverse_lazy('transactiontype_list_view')

class TransactionTypeDeleteView(DeleteView):
    model = TransactionType
    template_name = 'transactiontype/transactiontype_confirm_delete.html'
    success_url = reverse_lazy('transactiontype_list_view')

# Transaction CRUD
class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction/transaction_list.html'
    context_object_name = 'transactions'

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/transaction_form.html'
    success_url = reverse_lazy('transaction_list_view')

# UserSquad CRUD
class UserSquadListView(ListView):
    model = UserSquad
    template_name = 'usersquad/usersquad_list.html'
    context_object_name = 'squads'

class UserSquadCreateView(CreateView):
    model = UserSquad
    form_class = UserSquadForm
    template_name = 'usersquad/usersquad_form.html'
    success_url = reverse_lazy('usersquad_list_view')

# SquadPosition CRUD
class SquadPositionUpdateView(UpdateView):
    model = SquadPosition
    form_class = SquadPositionForm
    template_name = 'squadposition/squadposition_form.html'
    success_url = reverse_lazy('usersquad_list_view')

# SBCDifficulty CRUD
class SBCDifficultyListView(ListView):
    model = SBCDifficulty
    template_name = 'sbcdifficulty/sbcdifficulty_list.html'
    context_object_name = 'difficulties'

class SBCDifficultyCreateView(CreateView):
    model = SBCDifficulty
    form_class = SBCDifficultyForm
    template_name = 'sbcdifficulty/sbcdifficulty_form.html'
    success_url = reverse_lazy('sbcdifficulty_list_view')

class SBCDifficultyUpdateView(UpdateView):
    model = SBCDifficulty
    form_class = SBCDifficultyForm
    template_name = 'sbcdifficulty/sbcdifficulty_form.html'
    success_url = reverse_lazy('sbcdifficulty_list_view')

class SBCDifficultyDeleteView(DeleteView):
    model = SBCDifficulty
    template_name = 'sbcdifficulty/sbcdifficulty_confirm_delete.html'
    success_url = reverse_lazy('sbcdifficulty_list_view')

# SBC CRUD
class SBCListView(ListView):
    model = SBC
    template_name = 'sbc/sbc_list.html'
    context_object_name = 'sbcs'

class SBCCreateView(CreateView):
    model = SBC
    form_class = SBCForm
    template_name = 'sbc/sbc_form.html'
    success_url = reverse_lazy('sbc_list_view')

class SBCDetailView(DetailView):
    model = SBC
    template_name = 'sbc/sbc_detail.html'
    context_object_name = 'sbc'

# SBCReward CRUD
class SBCRewardListView(ListView):
    model = SBCReward
    template_name = 'sbcreward/sbcreward_list.html'
    context_object_name = 'rewards'

class SBCRewardCreateView(CreateView):
    model = SBCReward
    form_class = SBCRewardForm
    template_name = 'sbcreward/sbcreward_form.html'
    success_url = reverse_lazy('sbcreward_list_view')

class SBCRewardUpdateView(UpdateView):
    model = SBCReward
    form_class = SBCRewardForm
    template_name = 'sbcreward/sbcreward_form.html'
    success_url = reverse_lazy('sbcreward_list_view')

class SBCRewardDeleteView(DeleteView):
    model = SBCReward
    template_name = 'sbcreward/sbcreward_confirm_delete.html'
    success_url = reverse_lazy('sbcreward_list_view')

# SBCRequirement CRUD
class SBCRequirementListView(ListView):
    model = SBCRequirement
    template_name = 'sbcrequirement/sbcrequirement_list.html'
    context_object_name = 'requirements'

class SBCRequirementCreateView(CreateView):
    model = SBCRequirement
    form_class = SBCRequirementForm
    template_name = 'sbcrequirement/sbcrequirement_form.html'
    success_url = reverse_lazy('sbcrequirement_list_view')

class SBCRequirementUpdateView(UpdateView):
    model = SBCRequirement
    form_class = SBCRequirementForm
    template_name = 'sbcrequirement/sbcrequirement_form.html'
    success_url = reverse_lazy('sbcrequirement_list_view')

class SBCRequirementDeleteView(DeleteView):
    model = SBCRequirement
    template_name = 'sbcrequirement/sbcrequirement_confirm_delete.html'
    success_url = reverse_lazy('sbcrequirement_list_view')
    



@login_required
def create_player_card(request):
    if request.method == 'POST':
        form = PlayerCreationForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('my_club')
    else:
        form = PlayerCreationForm(user=request.user)
    return render(request, 'create_player.html', {'form': form})

@login_required
def my_club(request):
    created_players = Player.objects.filter(created_by=request.user)
    owned_players = Player.objects.filter(owner=request.user)

    # Отладка: Проверка наличия статистики
    print("Created Players:")
    for player in created_players:
        print(f"  Игрок: {player.name}, ID: {player.id}")
        if hasattr(player, 'stats'):
            print(f"    Статистика: Скорость={player.stats.pace}, Удары={player.stats.shooting}, Передачи={player.stats.passing}, Дриблинг={player.stats.dribbling}, Защита={player.stats.defending}, Физика={player.stats.physicality}, СлабаяНога={player.stats.weak_foot}, Финты={player.stats.skill_moves}")
        else:
            print("    Объект статистики не найден.")

    print("Owned Players:")
    for player in owned_players:
        print(f"  Игрок: {player.name}, ID: {player.id}")
        if hasattr(player, 'stats'):
            print(f"    Статистика: Скорость={player.stats.pace}, Удары={player.stats.shooting}, Передачи={player.stats.passing}, Дриблинг={player.stats.dribbling}, Защита={player.stats.defending}, Физика={player.stats.physicality}, СлабаяНога={player.stats.weak_foot}, Финты={player.stats.skill_moves}")
        else:
            print("    Объект статистики не найден.")

    return render(request, 'my_club.html', {'created_players': created_players, 'owned_players': owned_players})


@login_required
def buy_player(request, listing_id):
    listing = get_object_or_404(TransferListing, id=listing_id)
    if request.method == 'POST':
        if listing.buy_now_price and listing.status.name == 'Active':
            if request.user.coins >= listing.buy_now_price:
                
                listing.player.owner = request.user
                listing.player.save()
                
                request.user.coins -= listing.buy_now_price
                request.user.save()

                # Увеличение монет продавца
                seller_user = listing.seller
                seller_user.coins += listing.buy_now_price
                seller_user.save()

                listing.status = ListingStatus.objects.get(name='Sold')
                listing.save()
                
                Transaction.objects.create(
                    user=request.user,
                    player=listing.player,
                    price=listing.buy_now_price,
                    type=TransactionType.objects.get(name='Purchase')
                )
                return redirect('my_club')
            else:
                return render(request, 'error.html', {'message': 'Недостаточно монет для покупки'})
        else:
            return render(request, 'error.html', {'message': 'Листинг не активен или недоступен для покупки'})
    return render(request, 'confirm_purchase.html', {'listing': listing})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'info_view')
            return redirect(next_url)
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')

@login_required
def transfer_market_view(request):
    active_status = ListingStatus.objects.get(name='Active')
    active_listings = TransferListing.objects.filter(status=active_status).select_related('player__stats', 'player__position', 'player__nation', 'player__club')

    for listing in active_listings:
        time_since_last_update = timezone.now() - listing.last_price_update
        if time_since_last_update.total_seconds() > 300:  # 300 секунд = 5 минут
            new_price = random.randint(50000, 100000000)
            listing.buy_now_price = new_price
            listing.last_price_update = timezone.now()
            listing.save()

    return render(request, 'transfer.html', {'listings': active_listings})

@login_required
def sell_player(request, player_id):
    player = get_object_or_404(Player, id=player_id, owner=request.user) # Убедимся, что игрок принадлежит пользователю
    if request.method == 'POST':
        form = SellPlayerForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.player = player
            listing.seller = request.user
            listing.status = ListingStatus.objects.get(name='Active') # Устанавливаем статус Активно
            listing.save()
            messages.success(request, f'{player.name} успешно выставлен на трансферный рынок!')
            return redirect('my_club') # Или на страницу рынка
    else:
        form = SellPlayerForm()
    return render(request, 'sell_player.html', {'form': form, 'player': player})