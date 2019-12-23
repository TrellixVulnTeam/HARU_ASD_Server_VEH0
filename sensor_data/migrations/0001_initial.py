# Generated by Django 2.2.4 on 2019-10-26 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='unlocked_dur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('timestamp_end', models.BigIntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='total_dist_covered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('timestamp_end', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
                ('ema_order', models.SmallIntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='step_detector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='stddev_of_displacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('activity_type', models.CharField(default='', max_length=10)),
                ('confidence', models.FloatField(default=0.0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='stationary_dur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('timestamp_end', models.BigIntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='significant_motion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='radius_of_gyration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('timestamp_end', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
                ('ema_order', models.SmallIntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='phone_calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('timestamp_end', models.BigIntegerField(default=0)),
                ('call_type', models.TextField(blank=True, default='')),
                ('duration', models.IntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='num_of_dif_places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('timestamp_end', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
                ('ema_order', models.SmallIntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='max_dist_two_locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('timestamp_end', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
                ('ema_order', models.SmallIntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='max_dist_from_home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('timestamp_end', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
                ('ema_order', models.SmallIntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='light_intensity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='hrm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='gps_locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('lat', models.FloatField(default=0.0)),
                ('lng', models.FloatField(default=0.0)),
                ('accuracy', models.FloatField(default=0.0)),
                ('altitude', models.FloatField(default=0.0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='geofencing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_enter', models.BigIntegerField(default=0)),
                ('timestamp_exit', models.BigIntegerField(default=0)),
                ('location', models.CharField(default='', max_length=10)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='app_usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.BigIntegerField(default=0)),
                ('pkg_name', models.TextField(blank=True, default='')),
                ('app_name', models.TextField(blank=True, default='')),
                ('duration', models.IntegerField(default=0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('activity_type', models.CharField(default='', max_length=10)),
                ('confidence', models.FloatField(default=0.0)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='acc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value_x', models.TextField(blank=True, default='')),
                ('value_y', models.TextField(blank=True, default='')),
                ('value_z', models.TextField(blank=True, default='')),
                ('device', models.CharField(default='', max_length=10)),
                ('day_num', models.SmallIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
    ]
