from django.db import models

class Portfolio(models.Model):
    EXPIRY_CHOICES = (
        ('monthly_exp', 'Monthly Expiry'),
        ('weekly_exp', 'Weekly Expiry'),
        ('monthly_exp', 'Monthly Expiry'),
    )
    name = models.CharField(max_length=255)
    expiry = models.CharField(max_length=50, choices=EXPIRY_CHOICES)
    premium_gap = models.FloatField(null=True, blank=True)
    start = models.TimeField()
    end = models.TimeField()
    target = models.FloatField()
    stop_loss = models.FloatField()

class LegSettings(models.Model):
    STATE_CHOICES = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    RIGHT_CHOICES = (
        ('C', 'Call'),
        ('P', 'Put'),
    )
    TXN_CHOICES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )
    portfolio = models.ForeignKey(Portfolio, related_name='leg_settings', on_delete=models.CASCADE)
    state = models.IntegerField(choices=STATE_CHOICES)
    right = models.CharField(max_length=1, choices=RIGHT_CHOICES)
    txn = models.CharField(max_length=4, choices=TXN_CHOICES)
    execution_time = models.TimeField(null=True, blank=True)
    sqoff_time = models.TimeField(null=True, blank=True)
    count_sl = models.IntegerField()
    count_tp = models.IntegerField()
    wait_n_trade = models.IntegerField(null=True, blank=True)
    target_premium = models.FloatField()
    stop_loss = models.FloatField(null=True, blank=True)
    take_profit = models.FloatField(null=True, blank=True)
    ProfitLockThreshold = models.FloatField(null=True, blank=True)
    LockProfitAt = models.FloatField(null=True, blank=True)
    IncreaseInProfitForTrail = models.FloatField(null=True, blank=True)
    TrailProfitBy = models.FloatField(null=True, blank=True)
    SL_TrailTrigger = models.FloatField(null=True, blank=True)
    SL_Trail_Amt = models.FloatField(null=True, blank=True)
    
