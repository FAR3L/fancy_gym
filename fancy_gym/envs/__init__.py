from copy import deepcopy

import numpy as np
from gymnasium import register as gym_register
from .registry import register, ALL_FANCY_MOVEMENT_PRIMITIVE_ENVIRONMENTS

from . import classic_control, mujoco
from .classic_control.simple_reacher.simple_reacher import SimpleReacherEnv
from .classic_control.simple_reacher import MPWrapper as MPWrapper_SimpleReacher
from .classic_control.hole_reacher.hole_reacher import HoleReacherEnv
from .classic_control.hole_reacher import MPWrapper as MPWrapper_HoleReacher
from .classic_control.viapoint_reacher.viapoint_reacher import ViaPointReacherEnv
from .classic_control.viapoint_reacher import MPWrapper as MPWrapper_ViaPointReacher
from .mujoco.reacher.reacher import ReacherEnv, MAX_EPISODE_STEPS_REACHER
from .mujoco.reacher.mp_wrapper import MPWrapper as MPWrapper_Reacher
from .mujoco.ant_jump.ant_jump import MAX_EPISODE_STEPS_ANTJUMP
from .mujoco.beerpong.beerpong import MAX_EPISODE_STEPS_BEERPONG, FIXED_RELEASE_STEP
from .mujoco.half_cheetah_jump.half_cheetah_jump import MAX_EPISODE_STEPS_HALFCHEETAHJUMP
from .mujoco.hopper_jump.hopper_jump import MAX_EPISODE_STEPS_HOPPERJUMP
from .mujoco.hopper_jump.hopper_jump_on_box import MAX_EPISODE_STEPS_HOPPERJUMPONBOX
from .mujoco.hopper_throw.hopper_throw import MAX_EPISODE_STEPS_HOPPERTHROW
from .mujoco.hopper_throw.hopper_throw_in_basket import MAX_EPISODE_STEPS_HOPPERTHROWINBASKET
from .mujoco.walker_2d_jump.walker_2d_jump import MAX_EPISODE_STEPS_WALKERJUMP
from .mujoco.box_pushing.box_pushing_env import BoxPushingDense, BoxPushingTemporalSparse, \
    BoxPushingTemporalSpatialSparse, MAX_EPISODE_STEPS_BOX_PUSHING
from .mujoco.table_tennis.table_tennis_env import TableTennisEnv, TableTennisWind, TableTennisGoalSwitching, \
    MAX_EPISODE_STEPS_TABLE_TENNIS

# Classic Control
# Simple Reacher
register(
    id='SimpleReacher-v0',
    entry_point=SimpleReacherEnv,
    mp_wrapper=MPWrapper_SimpleReacher,
    max_episode_steps=200,
    kwargs={
        "n_links": 2,
    }
)

register(
    id='LongSimpleReacher-v0',
    entry_point=SimpleReacherEnv,
    mp_wrapper=MPWrapper_SimpleReacher,
    max_episode_steps=200,
    kwargs={
        "n_links": 5,
    }
)

# Viapoint Reacher
register(
    id='ViaPointReacher-v0',
    entry_point=ViaPointReacherEnv,
    mp_wrapper=MPWrapper_ViaPointReacher,
    max_episode_steps=200,
    kwargs={
        "n_links": 5,
        "allow_self_collision": False,
        "collision_penalty": 1000
    }
)

# Hole Reacher
register(
    id='HoleReacher-v0',
    entry_point=HoleReacherEnv,
    mp_wrapper=MPWrapper_HoleReacher,
    max_episode_steps=200,
    kwargs={
        "n_links": 5,
        "random_start": True,
        "allow_self_collision": False,
        "allow_wall_collision": False,
        "hole_width": None,
        "hole_depth": 1,
        "hole_x": None,
        "collision_penalty": 100,
    }
)

# Mujoco

# Mujoco Reacher
for dims in [5, 7]:
    register(
        id=f'Reacher{dims}d-v0',
        entry_point=ReacherEnv,
        mp_wrapper=MPWrapper_Reacher,
        max_episode_steps=MAX_EPISODE_STEPS_REACHER,
        kwargs={
            "n_links": dims,
        }
    )

    register(
        id=f'Reacher{dims}dSparse-v0',
        entry_point=ReacherEnv,
        mp_wrapper=MPWrapper_Reacher,
        max_episode_steps=MAX_EPISODE_STEPS_REACHER,
        kwargs={
            "sparse": True,
            'reward_weight': 200,
            "n_links": dims,
        }
    )


register(
    id='HopperJumpSparse-v0',
    entry_point='fancy_gym.envs.mujoco:HopperJumpEnv',
    mp_wrapper=mujoco.hopper_jump.MPWrapper,
    max_episode_steps=MAX_EPISODE_STEPS_HOPPERJUMP,
    kwargs={
        "sparse": True,
    }
)

register(
    id='HopperJump-v0',
    entry_point='fancy_gym.envs.mujoco:HopperJumpEnv',
    mp_wrapper=mujoco.hopper_jump.MPWrapper,
    max_episode_steps=MAX_EPISODE_STEPS_HOPPERJUMP,
    kwargs={
        "sparse": False,
        "healthy_reward": 1.0,
        "contact_weight": 0.0,
        "height_weight": 3.0,
    }
)

gym_register(
    id='AntJump-v0',
    entry_point='fancy_gym.envs.mujoco:AntJumpEnv',
    max_episode_steps=MAX_EPISODE_STEPS_ANTJUMP,
)

gym_register(
    id='HalfCheetahJump-v0',
    entry_point='fancy_gym.envs.mujoco:HalfCheetahJumpEnv',
    max_episode_steps=MAX_EPISODE_STEPS_HALFCHEETAHJUMP,
)

gym_register(
    id='HopperJumpOnBox-v0',
    entry_point='fancy_gym.envs.mujoco:HopperJumpOnBoxEnv',
    max_episode_steps=MAX_EPISODE_STEPS_HOPPERJUMPONBOX,
)

gym_register(
    id='HopperThrow-v0',
    entry_point='fancy_gym.envs.mujoco:HopperThrowEnv',
    max_episode_steps=MAX_EPISODE_STEPS_HOPPERTHROW,
)

gym_register(
    id='HopperThrowInBasket-v0',
    entry_point='fancy_gym.envs.mujoco:HopperThrowInBasketEnv',
    max_episode_steps=MAX_EPISODE_STEPS_HOPPERTHROWINBASKET,
)

gym_register(
    id='Walker2DJump-v0',
    entry_point='fancy_gym.envs.mujoco:Walker2dJumpEnv',
    max_episode_steps=MAX_EPISODE_STEPS_WALKERJUMP,
)

gym_register(
    id='BeerPong-v0',
    entry_point='fancy_gym.envs.mujoco:BeerPongEnv',
    max_episode_steps=MAX_EPISODE_STEPS_BEERPONG,
)

# Box pushing environments with different rewards
for reward_type in ["Dense", "TemporalSparse", "TemporalSpatialSparse"]:
    register(
        id='BoxPushing{}-v0'.format(reward_type),
        entry_point='fancy_gym.envs.mujoco:BoxPushing{}'.format(reward_type),
        mp_wrapper=mujoco.box_pushing.MPWrapper,
        max_episode_steps=MAX_EPISODE_STEPS_BOX_PUSHING,
    )

    register(
        id='BoxPushing{}Replan-v0'.format(reward_type),
        entry_point='fancy_gym.envs.mujoco:BoxPushing{}'.format(reward_type),
        mp_wrapper=mujoco.box_pushing.ReplanMPWrapper,
        register_step_based=False,
        max_episode_steps=MAX_EPISODE_STEPS_BOX_PUSHING,
    )

# Here we use the same reward as in BeerPong-v0, but now consider after the release,
# only one time step, i.e. we simulate until the end of th episode
gym_register(
    id='BeerPongStepBased-v0',
    entry_point='fancy_gym.envs.mujoco:BeerPongEnvStepBasedEpisodicReward',
    max_episode_steps=FIXED_RELEASE_STEP,
)

# Table Tennis environments
for ctxt_dim in [2, 4]:
    gym_register(
        id='TableTennis{}D-v0'.format(ctxt_dim),
        entry_point='fancy_gym.envs.mujoco:TableTennisEnv',
        max_episode_steps=MAX_EPISODE_STEPS_TABLE_TENNIS,
        kwargs={
            "ctxt_dim": ctxt_dim,
            'frame_skip': 4,
        }
    )

gym_register(
    id='TableTennisWind-v0',
    entry_point='fancy_gym.envs.mujoco:TableTennisWind',
    max_episode_steps=MAX_EPISODE_STEPS_TABLE_TENNIS,
)

gym_register(
    id='TableTennisGoalSwitching-v0',
    entry_point='fancy_gym.envs.mujoco:TableTennisGoalSwitching',
    max_episode_steps=MAX_EPISODE_STEPS_TABLE_TENNIS,
    kwargs={
        'goal_switching_step': 99
    }
)


# Beerpong ProMP
_versions = ['BeerPong-v0']
for _v in _versions:
    _name = _v.split("-")
    _env_id = f'{_name[0]}ProMP-{_name[1]}'
    kwargs_dict_bp_promp = deepcopy(DEFAULT_BB_DICT_ProMP)
    kwargs_dict_bp_promp['wrappers'].append(mujoco.beerpong.MPWrapper)
    kwargs_dict_bp_promp['phase_generator_kwargs']['learn_tau'] = True
    kwargs_dict_bp_promp['controller_kwargs']['p_gains'] = np.array([1.5, 5, 2.55, 3, 2., 2, 1.25])
    kwargs_dict_bp_promp['controller_kwargs']['d_gains'] = np.array([0.02333333, 0.1, 0.0625, 0.08, 0.03, 0.03, 0.0125])
    kwargs_dict_bp_promp['basis_generator_kwargs']['num_basis'] = 2
    kwargs_dict_bp_promp['basis_generator_kwargs']['num_basis_zero_start'] = 2
    kwargs_dict_bp_promp['name'] = _v
    gym_register(
        id=_env_id,
        entry_point='fancy_gym.utils.make_env_helpers:make_bb_env_helper',
        kwargs=kwargs_dict_bp_promp
    )
    ALL_FANCY_MOVEMENT_PRIMITIVE_ENVIRONMENTS["ProMP"].append(_env_id)

# BP with Fixed release
_versions = ["BeerPongStepBased-v0", 'BeerPong-v0']
for _v in _versions:
    if _v != 'BeerPong-v0':
        _name = _v.split("-")
        _env_id = f'{_name[0]}ProMP-{_name[1]}'
    else:
        _env_id = 'BeerPongFixedReleaseProMP-v0'
    kwargs_dict_bp_promp = deepcopy(DEFAULT_BB_DICT_ProMP)
    kwargs_dict_bp_promp['wrappers'].append(mujoco.beerpong.MPWrapper)
    kwargs_dict_bp_promp['phase_generator_kwargs']['tau'] = 0.62
    kwargs_dict_bp_promp['controller_kwargs']['p_gains'] = np.array([1.5, 5, 2.55, 3, 2., 2, 1.25])
    kwargs_dict_bp_promp['controller_kwargs']['d_gains'] = np.array([0.02333333, 0.1, 0.0625, 0.08, 0.03, 0.03, 0.0125])
    kwargs_dict_bp_promp['basis_generator_kwargs']['num_basis'] = 2
    kwargs_dict_bp_promp['basis_generator_kwargs']['num_basis_zero_start'] = 2
    kwargs_dict_bp_promp['name'] = _v
    gym_register(
        id=_env_id,
        entry_point='fancy_gym.utils.make_env_helpers:make_bb_env_helper',
        kwargs=kwargs_dict_bp_promp
    )
    ALL_FANCY_MOVEMENT_PRIMITIVE_ENVIRONMENTS["ProMP"].append(_env_id)
########################################################################################################################

# Table Tennis needs to be fixed according to Zhou's implementation

# TODO: Add later when finished
# ########################################################################################################################
#
# ## AntJump
# _versions = ['AntJump-v0']
# for _v in _versions:
#     _name = _v.split("-")
#     _env_id = f'{_name[0]}ProMP-{_name[1]}'
#     kwargs_dict_ant_jump_promp = deepcopy(DEFAULT_BB_DICT_ProMP)
#     kwargs_dict_ant_jump_promp['wrappers'].append(mujoco.ant_jump.MPWrapper)
#     kwargs_dict_ant_jump_promp['name'] = _v
#     gym_register(
#         id=_env_id,
#         entry_point='fancy_gym.utils.make_env_helpers:make_bb_env_helper',
#         kwargs=kwargs_dict_ant_jump_promp
#     )
#     ALL_FANCY_MOVEMENT_PRIMITIVE_ENVIRONMENTS["ProMP"].append(_env_id)
#
# ########################################################################################################################
#
# ## HalfCheetahJump
# _versions = ['HalfCheetahJump-v0']
# for _v in _versions:
#     _name = _v.split("-")
#     _env_id = f'{_name[0]}ProMP-{_name[1]}'
#     kwargs_dict_halfcheetah_jump_promp = deepcopy(DEFAULT_BB_DICT_ProMP)
#     kwargs_dict_halfcheetah_jump_promp['wrappers'].append(mujoco.half_cheetah_jump.MPWrapper)
#     kwargs_dict_halfcheetah_jump_promp['name'] = _v
#     gym_register(
#         id=_env_id,
#         entry_point='fancy_gym.utils.make_env_helpers:make_bb_env_helper',
#         kwargs=kwargs_dict_halfcheetah_jump_promp
#     )
#     ALL_FANCY_MOVEMENT_PRIMITIVE_ENVIRONMENTS["ProMP"].append(_env_id)
#
# ########################################################################################################################

# Table Tennis
_versions = ['TableTennis2D-v0', 'TableTennis4D-v0', 'TableTennisWind-v0', 'TableTennisGoalSwitching-v0']
for _v in _versions:
    _name = _v.split("-")
    _env_id = f'{_name[0]}ProMP-{_name[1]}'
    kwargs_dict_tt_promp = deepcopy(DEFAULT_BB_DICT_ProMP)
    if _v == 'TableTennisWind-v0':
        kwargs_dict_tt_promp['wrappers'].append(mujoco.table_tennis.TTVelObs_MPWrapper)
    else:
        kwargs_dict_tt_promp['wrappers'].append(mujoco.table_tennis.TT_MPWrapper)
    kwargs_dict_tt_promp['name'] = _v
    kwargs_dict_tt_promp['controller_kwargs']['p_gains'] = 0.5 * np.array([1.0, 4.0, 2.0, 4.0, 1.0, 4.0, 1.0])
    kwargs_dict_tt_promp['controller_kwargs']['d_gains'] = 0.5 * np.array([0.1, 0.4, 0.2, 0.4, 0.1, 0.4, 0.1])
    kwargs_dict_tt_promp['phase_generator_kwargs']['learn_tau'] = False
    kwargs_dict_tt_promp['phase_generator_kwargs']['learn_delay'] = False
    kwargs_dict_tt_promp['phase_generator_kwargs']['tau_bound'] = [0.8, 1.5]
    kwargs_dict_tt_promp['phase_generator_kwargs']['delay_bound'] = [0.05, 0.15]
    kwargs_dict_tt_promp['basis_generator_kwargs']['num_basis'] = 3
    kwargs_dict_tt_promp['basis_generator_kwargs']['num_basis_zero_start'] = 1
    kwargs_dict_tt_promp['basis_generator_kwargs']['num_basis_zero_goal'] = 1
    kwargs_dict_tt_promp['black_box_kwargs']['verbose'] = 2
    gym_register(
        id=_env_id,
        entry_point='fancy_gym.utils.make_env_helpers:make_bb_env_helper',
        kwargs=kwargs_dict_tt_promp
    )
    ALL_FANCY_MOVEMENT_PRIMITIVE_ENVIRONMENTS["ProMP"].append(_env_id)

for _v in _versions:
    _name = _v.split("-")
    _env_id = f'{_name[0]}ProDMP-{_name[1]}'
    kwargs_dict_tt_prodmp = deepcopy(DEFAULT_BB_DICT_ProDMP)
    if _v == 'TableTennisWind-v0':
        kwargs_dict_tt_prodmp['wrappers'].append(mujoco.table_tennis.TTVelObs_MPWrapper)
    else:
        kwargs_dict_tt_prodmp['wrappers'].append(mujoco.table_tennis.TT_MPWrapper)
    kwargs_dict_tt_prodmp['name'] = _v
    kwargs_dict_tt_prodmp['controller_kwargs']['p_gains'] = 0.5 * np.array([1.0, 4.0, 2.0, 4.0, 1.0, 4.0, 1.0])
    kwargs_dict_tt_prodmp['controller_kwargs']['d_gains'] = 0.5 * np.array([0.1, 0.4, 0.2, 0.4, 0.1, 0.4, 0.1])
    kwargs_dict_tt_prodmp['trajectory_generator_kwargs']['weights_scale'] = 0.7
    kwargs_dict_tt_prodmp['trajectory_generator_kwargs']['auto_scale_basis'] = True
    kwargs_dict_tt_prodmp['trajectory_generator_kwargs']['relative_goal'] = True
    kwargs_dict_tt_prodmp['trajectory_generator_kwargs']['disable_goal'] = True
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['tau_bound'] = [0.8, 1.5]
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['delay_bound'] = [0.05, 0.15]
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['learn_tau'] = True
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['learn_delay'] = True
    kwargs_dict_tt_prodmp['basis_generator_kwargs']['num_basis'] = 3
    kwargs_dict_tt_prodmp['basis_generator_kwargs']['alpha'] = 25.
    kwargs_dict_tt_prodmp['basis_generator_kwargs']['basis_bandwidth_factor'] = 3
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['alpha_phase'] = 3
    gym_register(
        id=_env_id,
        entry_point='fancy_gym.utils.make_env_helpers:make_bb_env_helper',
        kwargs=kwargs_dict_tt_prodmp
    )
    ALL_FANCY_MOVEMENT_PRIMITIVE_ENVIRONMENTS["ProDMP"].append(_env_id)

for _v in _versions:
    _name = _v.split("-")
    _env_id = f'{_name[0]}ReplanProDMP-{_name[1]}'
    kwargs_dict_tt_prodmp = deepcopy(DEFAULT_BB_DICT_ProDMP)
    if _v == 'TableTennisWind-v0':
        kwargs_dict_tt_prodmp['wrappers'].append(mujoco.table_tennis.TTVelObs_MPWrapper)
    else:
        kwargs_dict_tt_prodmp['wrappers'].append(mujoco.table_tennis.TT_MPWrapper)
    kwargs_dict_tt_prodmp['name'] = _v
    kwargs_dict_tt_prodmp['controller_kwargs']['p_gains'] = 0.5 * np.array([1.0, 4.0, 2.0, 4.0, 1.0, 4.0, 1.0])
    kwargs_dict_tt_prodmp['controller_kwargs']['d_gains'] = 0.5 * np.array([0.1, 0.4, 0.2, 0.4, 0.1, 0.4, 0.1])
    kwargs_dict_tt_prodmp['trajectory_generator_kwargs']['auto_scale_basis'] = False
    kwargs_dict_tt_prodmp['trajectory_generator_kwargs']['goal_offset'] = 1.0
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['tau_bound'] = [0.8, 1.5]
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['delay_bound'] = [0.05, 0.15]
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['learn_tau'] = True
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['learn_delay'] = True
    kwargs_dict_tt_prodmp['basis_generator_kwargs']['num_basis'] = 2
    kwargs_dict_tt_prodmp['basis_generator_kwargs']['alpha'] = 25.
    kwargs_dict_tt_prodmp['basis_generator_kwargs']['basis_bandwidth_factor'] = 3
    kwargs_dict_tt_prodmp['phase_generator_kwargs']['alpha_phase'] = 3
    kwargs_dict_tt_prodmp['black_box_kwargs']['max_planning_times'] = 3
    kwargs_dict_tt_prodmp['black_box_kwargs']['replanning_schedule'] = lambda pos, vel, obs, action, t: t % 50 == 0
    gym_register(
        id=_env_id,
        entry_point='fancy_gym.utils.make_env_helpers:make_bb_env_helper',
        kwargs=kwargs_dict_tt_prodmp
    )
    ALL_FANCY_MOVEMENT_PRIMITIVE_ENVIRONMENTS["ProDMP"].append(_env_id)
