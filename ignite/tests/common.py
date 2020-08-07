# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
from datadog_checks.dev.jmx import JVM_E2E_METRICS

GAUGES = [
    'ignite.cache.offheap_miss_percentage',
    'ignite.jobs.wait_time.maximum',
    'ignite.cache.size',
    'ignite.cache.entry_processor.hit_percentage',
    'ignite.cache.start_version_counts_size',
    'ignite.discovery.message_worker_queue_size',
    'ignite.pages_replace_rate',
    'ignite.non_heap_memory_initialized',
    'ignite.discovery.average_message_processing_time',
    'ignite.current_idle_time',
    'ignite.jobs.cancelled.current',
    'ignite.cache.local_renting_partitions',
    'ignite.cache.average_rollback_time',
    'ignite.current_daemon_thread_count',
    'ignite.cache.rebalance_clearing_partitions',
    'ignite.heap_memory_committed',
    'ignite.cache.rebalancing_keys_rate',
    'ignite.total_server_nodes',
    'ignite.cache.cluster_owning_partitions',
    'ignite.checkpoint.last_pages_write_duration',
    'ignite.cache.offheap_allocated_size',
    'ignite.cache.thread_map_size',
    'ignite.dirty_pages',
    'ignite.cache.average_put_time',
    'ignite.cache.average_get_time',
    'ignite.cache.average_commit_time',
    'ignite.cache.entry_processor.miss_percentage',
    'ignite.cache.rebalancing_partitions',
    'ignite.jobs.execute_time.average',
    'ignite.total_client_nodes',
    'ignite.wal.archive_segments',
    'ignite.current_cpu_load',
    'ignite.cache.average_remove_time',
    'ignite.cache.offheap_backup_entries',
    'ignite.wal.total_size',
    'ignite.threads.pool_size',
    'ignite.used_checkpoint_buffer_pages',
    'ignite.jobs.wait_time.current',
    'ignite.offheap_size',
    'ignite.current_thread_count',
    'ignite.average_cpu_load',
    'ignite.cache.xid_map_size',
    'ignite.cache.rebalancing_bytes_rate',
    'ignite.checkpoint.last_lock_wait_duration',
    'ignite.offheap_used_size',
    'ignite.threads.largest_size',
    'ignite.cache.dht_committed_versions_size',
    'ignite.threads.maximum_pool_size',
    'ignite.pages_fill_factor',
    'ignite.cache.offheap_primary_entries',
    'ignite.cache.miss_percentage',
    'ignite.cache.commit_queue_size',
    'ignite.cache.dht_prepare_queue_size',
    'ignite.cache.dht_commit_queue_size',
    'ignite.heap_memory_initialized',
    'ignite.total_cpus',
    'ignite.jobs.active.maximum',
    'ignite.checkpoint.last_data_pages',
    'ignite.used_checkpoint_buffer_size',
    'ignite.checkpoint.last_total_pages',
    'ignite.total_nodes',
    'ignite.eviction_rate',
    'ignite.oubound_messages_queue_size',
    'ignite.jobs.execute_time.current',
    'ignite.threads.queue_size',
    'ignite.discovery.pending_messages_registered',
    'ignite.cache.keys_to_rebalance',
    'ignite.transaction.locked_keys',
    'ignite.discovery.pending_messages_discarded',
    'ignite.cache.dht_rolledback_versions_size',
    'ignite.checkpoint.last_mark_duration',
    'ignite.max_memory_size',
    'ignite.checkpoint.last_fsync_duration',
    'ignite.cache.rolledback_versions_size',
    'ignite.transaction.owner',
    'ignite.cache.offheap_entries',
    'ignite.wal.writing_rate',
    'ignite.cache.estimated_rebalancing_keys',
    'ignite.cache.heap_entries',
    'ignite.total_idle_time',
    'ignite.cache.maximum_partition_copies',
    'ignite.idle_time_percentage',
    'ignite.checkpoint.total_time',
    'ignite.cache.hit_percentage',
    'ignite.jobs.waiting.current',
    'ignite.cache.minimum_partition_copies',
    'ignite.non_heap_memory_used',
    'ignite.maximum_thread_count',
    'ignite.jobs.rejected.maximum',
    'ignite.initial_memory_size',
    'ignite.cache.write_behind_overflow',
    'ignite.active_baseline_nodes',
    'ignite.heap_memory_total',
    'ignite.cache.local_renting_entries',
    'ignite.cache.prepare_queue_size',
    'ignite.cache.dht_thread_map_size',
    'ignite.jobs.rejected.current',
    'ignite.cache.write_behind_store_batch_size',
    'ignite.cache.local_owning_partitions',
    'ignite.jobs.active.current',
    'ignite.jobs.rejected.average',
    'ignite.cache.entry_processor.average_invocation_time',
    'ignite.jobs.execute_time.maximum',
    'ignite.cache.write_behind_retries',
    'ignite.threads.active',
    'ignite.checkpoint.last_duration',
    'ignite.cache.entry_processor.maximum_invocation_time',
    'ignite.current_gc_load',
    'ignite.heap_memory_used',
    'ignite.check_point_buffer_size',
    'ignite.wal.buffer_poll_spin',
    'ignite.allocation_rate',
    'ignite.jobs.waiting.maximum',
    'ignite.wal.fsync_average',
    'ignite.transaction.holding_lock',
    'ignite.threads.core_pool_size',
    'ignite.cache.partitions',
    'ignite.jobs.cancelled.maximum',
    'ignite.large_entries_pages_percentage',
    'ignite.non_heap_memory_maximum',
    'ignite.pages_replace_age',
    'ignite.busy_time_percentage',
    'ignite.jobs.cancelled.average',
    'ignite.physical_memory_pages',
    'ignite.non_heap_memory_total',
    'ignite.cache.evict_queue_size',
    'ignite.cache.write_behind_buffer_size',
    'ignite.cache.entry_processor.minimum_invocation_time',
    'ignite.cache.dht_start_version_counts_size',
    'ignite.cache.local_moving_partitions',
    'ignite.wal.logging_rate',
    'ignite.cache.rebalanced_keys',
    'ignite.jobs.maximum_failover',
    'ignite.cache.committed_versions_size',
    'ignite.total_baseline_nodes',
    'ignite.cache.cluster_moving_partitions',
    'ignite.cache.offheap_hit_percentage',
    'ignite.jobs.active.average',
    'ignite.cache.dht_xid_map_size',
    'ignite.cache.backups',
    'ignite.heap_memory_maximum',
    'ignite.jobs.wait_time.average',
    'ignite.discovery.max_message_processing_time',
    'ignite.total_busy_time',
    'ignite.cache.total_partitions',
    'ignite.non_heap_memory_committed',
    'ignite.jobs.waiting.average',
    'ignite.checkpoint.last_copied_on_write_pages',
    'ignite.wal.last_rollover',
] + JVM_E2E_METRICS

MONOTONIC_COUNTS = [
    "ignite.cache.commits",
    "ignite.cache.entry_processor.hits",
    "ignite.cache.entry_processor.invocations",
    "ignite.cache.entry_processor.misses",
    "ignite.cache.entry_processor.puts",
    "ignite.cache.entry_processor.read_only_invocations",
    "ignite.cache.entry_processor.removals",
    "ignite.cache.evictions",
    "ignite.cache.gets",
    "ignite.cache.hits",
    "ignite.cache.misses",
    "ignite.cache.offheap_evictions",
    "ignite.cache.offheap_gets",
    "ignite.cache.offheap_hits",
    "ignite.cache.offheap_misses",
    "ignite.cache.offheap_puts",
    "ignite.cache.offheap_removals",
    "ignite.cache.puts",
    "ignite.cache.removals",
    "ignite.cache.rollbacks",
    "ignite.cache.write_behind_overflow_total",
    "ignite.discovery.nodes_failed",
    "ignite.discovery.nodes_joined",
    "ignite.discovery.nodes_left",
    "ignite.discovery.total_processed_messages",
    "ignite.discovery.total_received_messages",
    "ignite.jobs.cancelled.total",
    "ignite.jobs.executed.total",
    "ignite.jobs.execution_time.total",
    "ignite.jobs.rejected.total",
    "ignite.jobs.total_failover",
    "ignite.pages_read",
    "ignite.pages_replaced",
    "ignite.pages_written",
    "ignite.received_bytes",
    "ignite.received_messages",
    "ignite.sent_bytes",
    "ignite.sent_messages",
    "ignite.threads.completed_tasks",
    "ignite.threads.tasks",
    "ignite.total_allocated_pages",
    "ignite.total_allocated_size",
    "ignite.total_executed_tasks",
    "ignite.total_started_threads",
    "ignite.transaction.committed",
    "ignite.transaction.rolledback",
]
