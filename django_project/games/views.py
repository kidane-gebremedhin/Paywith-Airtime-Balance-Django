from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from club.models import Club
from game_prices.models import GamePrice

from home_or_away_status.models import HomeOrAwayStatus
from .models import Game

def upcoming_games(self):
	clubs=Club.objects.all().values()
	home_or_away_status=HomeOrAwayStatus.objects.all().values()
	
	games_option=[]
	games=Game.objects.all()#.values()
	for game in games:
		games_price_option2=[]
		for gp in GamePrice.objects.filter(game=game):
			data={
				'id':f'{gp.id}',
				'name':f'{gp.priceType}',
				'priceInBirr':f'{gp.priceInBirr}',
				'game':f'{gp.game}',
			}
			games_price_option2.append(data)

		data={
			'id':f'{game.id}',
			'name':f'{game}',
			'stadium':f'{game.stadium}',
			'competetionType':f'{game.competetionType}',
			'round':f'{game.round}',
			'homeSide':f'{game.homeSide}',
			'awaySide':f'{game.awaySide}',
			'game_dateTime':f'{game.game_dateTime}',
			'accountNumber':f'{game.homeSide.accountNumber}',
			'game_prices':list(games_price_option2),
		}
		games_option.append(data)
	
	game_prices_option=[]
	game_prices=GamePrice.objects.all()#.values()
	for game_price in game_prices:
		data={
			'id':f'{game_price.id}',
			'name':f'{game_price.priceType}',
			'priceInBirr':f'{game_price.priceInBirr}',
			'game':f'{game_price.game}',
		}
		game_prices_option.append(data)

	responseData={
	'type':'data',
	'games_option':list(games_option),
	'games':list(games_option),

	'clubs':list(clubs),
	'home_or_away_status':list(home_or_away_status),
	}

	# for g in games:
	# 	print(f'{g.stadium}')
	return JsonResponse(responseData, safe=False)
                
